import json
import os
from pathlib import Path
from typing import List
from uuid import UUID
from typing import List

import requests
from PySide6.QtCore import QFile, QTextStream

from pkg.api.constants import OFFICIAL_DB_URL, CFG_DIR, CACHE_DIR, FILE_OFFICIAL_DB, FILE_THIRD_PARTY_DB, \
    STORY_TRANSCODING_SUPPORTED, OFFICIAL_TOKEN_URL

STORY_UNKNOWN  = "Unknown story (maybe a User created story)..."
DESC_NOT_FOUND = "No description found."
AUTHOR_NOT_FOUND = "No author found."

# https://server-data-prod.lunii.com/v2/packs
DB_OFFICIAL = {}
DB_THIRD_PARTY = {}

NODE_SIZE = 0x2C
NI_HEADER_SIZE = 0x200

FILE_THUMB = "_thumbnail.png"
FILE_META  = "_metadata.json"
FILE_UUID  = "uuid.bin"
FILE_STUDIO_JSON  = "story.json"
FILE_STUDIO_THUMB = "thumbnail.png"

class StudioStory:
    def __init__(self, story_json=None):
        self.format_version = 0
        self.pack_version = 0
        self.title = ""
        self.description = ""
        self.factory_pack = 1
        self.uuid = None
        self.nm = False # night mode

        self.js_snodes = None
        self.js_anodes = None
        self.ri = dict()
        self.si = dict()
        self.li: List[int] = list()

        # depends on ffmpeg presence on host system
        self.compatible = False

        if story_json:
            self.load(story_json)

    @property
    def name(self):
        return self.title

    @property
    def str_uuid(self):
        if self.uuid:
            return str(self.uuid).upper()
        return None

    @property
    def short_uuid(self):
        if self.uuid:
            return self.uuid.hex[24:].upper()
        return None
    
    def load(self, story_json):
        self.format_version = story_json.get('format')
        self.pack_version = story_json.get('version')
        self.title = story_json.get('title')
        self.description = story_json.get('description')
        self.nm = story_json.get('nightModeAvailable', False)

        # looping stage nodes
        self.js_snodes = story_json.get('stageNodes')
        for snode in self.js_snodes:
            n_uuid = UUID(snode.get('uuid'))
            if not self.uuid:
                self.uuid = n_uuid

            image = snode.get('image')
            if image:
                if image not in self.ri:
                    normalized_name = os.path.splitext(image)[0]
                    normalized_name = normalized_name[-8:].upper()
                    self.ri[image] = (normalized_name, len(self.ri))

            audio = snode.get('audio')
            if audio:
                if not STORY_TRANSCODING_SUPPORTED and not audio.lower().endswith('.mp3'):
                    self.compatible = False
                    return

                if audio not in self.si:
                    normalized_name = os.path.splitext(audio)[0]
                    normalized_name = normalized_name[-8:].upper()
                    self.si[audio] = (normalized_name, len(self.si))

        # looping action nodes
        absolute_index = 0
        self.js_anodes = story_json.get('actionNodes')
        for anode in self.js_anodes:
            anode["global_index"] = absolute_index
            absolute_index += len(anode.get("options"))
            for option in anode.get("options"):
                option_index = next((index for index, snode in enumerate(self.js_snodes) if snode.get('uuid') == option), -1)
                self.li.append(option_index)

        self.compatible = True

    def get_ri_data(self):
        data_ri = ""
        for file in self.ri:
            data_ri += f"000\\{self.ri[file][0]}"
        return data_ri.encode('utf-8')
    
    def get_si_data(self):
        data_si = ""
        for file in self.si:
            data_si += f"000\\{self.si[file][0]}"
        return data_si.encode('utf-8')
    
    def get_ni_data(self):
        ni_buffer = b""

        # header section
        ni_buffer += int(self.format_version[1:]).to_bytes(2, byteorder='little')
        ni_buffer += int(self.pack_version).to_bytes(2, byteorder='little')
        ni_buffer += int(NI_HEADER_SIZE).to_bytes(4, byteorder='little')
        ni_buffer += int(NODE_SIZE).to_bytes(4, byteorder='little')
        ni_buffer += len(self.js_snodes).to_bytes(4, byteorder='little')
        ni_buffer += len(self.ri).to_bytes(4, byteorder='little')
        ni_buffer += len(self.si).to_bytes(4, byteorder='little')
        ni_buffer += int(1).to_bytes(1, byteorder='little')

        # padding the header with 00
        ni_buffer += b"\x00" * (NI_HEADER_SIZE - len(ni_buffer))

        # node section
        for snode in self.js_snodes:
            current_node = b""

            # image / audio for nodes
            ri_index = -1
            si_index = -1
            if snode.get('image') in self.ri:
                ri_index = self.ri[snode.get('image')][1]
            if snode.get('audio') in self.si:
                si_index = self.si[snode.get('audio')][1]
            current_node += ri_index.to_bytes(4, byteorder='little', signed=True)
            current_node += si_index.to_bytes(4, byteorder='little', signed=True)
            
            # ok transition
            trans_node = snode.get("okTransition")
            if trans_node:
                # looking for action node
                anode_uuid = trans_node.get("actionNode")
                anode = next((one_node for one_node in self.js_anodes if one_node.get('id') == anode_uuid), -1)
                li_index = anode.get("global_index")
                # transition settings
                current_node += li_index.to_bytes(4, byteorder='little', signed=True)
                current_node += len(anode.get('options')).to_bytes(4, byteorder='little', signed=True)
                current_node += trans_node.get('optionIndex').to_bytes(4, byteorder='little', signed=True)
            else:
                current_node += b"\xFF\xFF\xFF\xFF" * 3

            # home transition
            trans_node = snode.get("homeTransition")
            if trans_node:
                # looking for action node
                anode_uuid = trans_node.get("actionNode")
                anode = next((one_node for one_node in self.js_anodes if one_node.get('id') == anode_uuid), -1)
                li_index = anode.get("global_index")
                # transition settings
                current_node += li_index.to_bytes(4, byteorder='little', signed=True)
                current_node += len(anode.get('options')).to_bytes(4, byteorder='little', signed=True)
                current_node += trans_node.get('optionIndex').to_bytes(4, byteorder='little', signed=True)
            else:
                current_node += b"\xFF\xFF\xFF\xFF" * 3

            # control section
            controls = snode.get("controlSettings")
            if controls:
                current_node += controls.get("wheel").to_bytes(2, byteorder="little")
                current_node += controls.get("ok").to_bytes(2, byteorder="little")
                current_node += controls.get("home").to_bytes(2, byteorder="little")
                current_node += controls.get("pause").to_bytes(2, byteorder="little")
                current_node += controls.get("autoplay").to_bytes(2, byteorder="little")
                current_node += b"\x00\x00"

            # FINAL : adding current node to list
            ni_buffer += current_node
            ni_buffer += b"\xAA" * (NODE_SIZE - len(current_node))

        return ni_buffer

    def get_li_data(self):
        li_buffer = b""

        # parsing list node index
        for index in self.li:
            # Write index as signed 4-byte integer (little endian)
            li_buffer += index.to_bytes(4, byteorder='little', signed=True)

        # adding extra padding for small stories
        while len(li_buffer) < 8:
            li_buffer += b"\x00"

        return li_buffer

    def write_bt(self, path_ni):
        pass


def story_load_db(reload=False):
    global DB_OFFICIAL
    global DB_THIRD_PARTY
    retVal = True

    # fetching db if necessary
    if not os.path.isfile(FILE_OFFICIAL_DB) or reload:
        # creating dir if not there
        if not os.path.isdir(CFG_DIR):
            Path(CFG_DIR).mkdir(parents=True, exist_ok=True)

        try:
            # Set the timeout for the request
            token_resp = requests.get(OFFICIAL_TOKEN_URL, timeout=30)
            if token_resp.status_code == 200:
                auth_token = token_resp.json()['response']['token']['server']

                req_headers = {"Application-Sender": "luniistore_desktop",
                               "Accept": "application/json",
                               'X-AUTH-TOKEN': auth_token,
                              }

                response = requests.get(OFFICIAL_DB_URL, headers=req_headers, timeout=30)
                if response.status_code == 200:
                    # Load image from bytes
                    j_resp = json.loads(response.content)
                    with (open(FILE_OFFICIAL_DB, "w") as fp):
                        db = j_resp.get('response')
                        json.dump(db, fp)

        except (requests.exceptions.Timeout, requests.exceptions.RequestException, requests.exceptions.ConnectionError):
            retVal = False

    # trying to load official DB
    if os.path.isfile(FILE_OFFICIAL_DB):
        try:
            with open(FILE_OFFICIAL_DB, encoding='utf-8') as fp_db:
                db_stories = json.load(fp_db)
                DB_OFFICIAL = {db_stories[key]["uuid"].upper(): value for (key, value) in db_stories.items()}
        except:
            db = Path(FILE_OFFICIAL_DB)
            db.unlink(FILE_OFFICIAL_DB)

    # trying to load third-party DB
    if not os.path.isfile(FILE_THIRD_PARTY_DB):
        # no local unofficial DB, creating the one from resource
        file = QFile(f":/json/res/unofficial.json")  # Use the alias defined in the .qrc file
        if file.open(QFile.ReadOnly | QFile.Text):
            textStream = QTextStream(file)
            content = textStream.readAll()
            file.close()

            # Write the content to a new file
            with open(FILE_THIRD_PARTY_DB, "w", encoding='utf-8') as f:
                f.write(content)

    # there should be an unofficial DB
    if os.path.isfile(FILE_THIRD_PARTY_DB):
        try:
            with open(FILE_THIRD_PARTY_DB, encoding='utf-8') as fp_db:
                db_stories = json.load(fp_db)
                DB_THIRD_PARTY = {db_stories[key]["uuid"].upper(): value for (key, value) in db_stories.items()}
        except:
            db = Path(FILE_THIRD_PARTY_DB)
            db.unlink(FILE_THIRD_PARTY_DB)

    return retVal


def thirdparty_db_add_thumb(uuid: UUID, image_data: bytes):
    # creating cache dir if necessary
    if not os.path.isdir(CACHE_DIR):
        Path(CACHE_DIR).mkdir(parents=True, exist_ok=True)

    # checking if present in cache
    one_uuid = str(uuid).upper()
    res_file = os.path.join(CACHE_DIR, one_uuid)

    if not os.path.isfile(res_file):
        # write data to file
        with open(res_file, "wb") as fp:
            fp.write(image_data)


def thirdparty_db_add_story(uuid: UUID, title: str, desc: str):
    db_stories = dict()

    # trying to load third-party DB
    if os.path.isfile(FILE_THIRD_PARTY_DB):
        try:
            with open(FILE_THIRD_PARTY_DB, encoding='utf-8') as fp_db:
                db_stories = json.load(fp_db)
        except:
            db = Path(FILE_THIRD_PARTY_DB)
            db.unlink(FILE_THIRD_PARTY_DB)

    # creating new entry
    db_stories[uuid.hex] = {'uuid': str(uuid), 'title': title, 'description': desc}

    # saving updated db
    with open(FILE_THIRD_PARTY_DB, "w", encoding='utf-8') as fp_db:
        json.dump(db_stories, fp_db)

    # reloading DBs
    story_load_db()


def _uuid_match(uuid: UUID, key_part: str):
    uuid = uuid.hex.upper()
    key_part = key_part.replace("-", "").upper()

    return key_part in uuid


class Story:
    def __init__(self, uuid: UUID, hidden: bool = False, nm = False, size: int = -1):
        self.uuid = uuid
        self.size = size
        self.hidden = hidden
        self.nm = nm

    def __eq__(self, __value: UUID):
        return self.uuid == __value

    @property
    def str_uuid(self):
        return str(self.uuid).upper()

    @property
    def short_uuid(self):
        return self.uuid.hex[24:].upper()

    @property
    def name(self):
        one_uuid = str(self.uuid).upper()

        for db in [DB_OFFICIAL, DB_THIRD_PARTY]:
            # checking current db
            if one_uuid in db:
                if db[one_uuid].get("locales_available") and db[one_uuid].get("localized_infos"):
                    locale = list(db[one_uuid]["locales_available"].keys())[0]
                    title = db[one_uuid]["localized_infos"][locale].get("title")
                    return title
                else:
                    title = db[one_uuid].get("title")
                    if title:
                        return title


        return STORY_UNKNOWN

    @property
    def desc(self):
        one_uuid = str(self.uuid).upper()

        for db in [DB_OFFICIAL, DB_THIRD_PARTY]:
            # checking current db
            if one_uuid in db:
                if db[one_uuid].get("locales_available") and db[one_uuid].get("localized_infos"):
                    locale = list(db[one_uuid]["locales_available"].keys())[0]
                    desc: str = db[one_uuid]["localized_infos"][locale].get("description")
                    # removing html parts
                    while desc.lstrip().startswith("<"):
                        pos = desc.find(">")
                        desc = desc[pos+1:].lstrip()
                    return desc
                else:
                    desc = db[one_uuid].get("description")
                    if desc:
                        return desc

        return DESC_NOT_FOUND

    @property
    def author(self):
        one_uuid = str(self.uuid).upper()

        for db in [DB_OFFICIAL, DB_THIRD_PARTY]:
            # checking current db
            if one_uuid in db:
                if db[one_uuid].get("authors"):
                    key = list(db[one_uuid]["authors"].keys())[0]
                    author: str = db[one_uuid]["authors"][key].get("name")
                    return author
                else:
                    author = db[one_uuid].get("author")
                    if author:
                        return author

        return AUTHOR_NOT_FOUND

    def get_picture(self, reload: bool = False):
        image_data = None

        # creating cache dir if necessary
        if not os.path.isdir(CACHE_DIR):
            Path(CACHE_DIR).mkdir(parents=True, exist_ok=True)

        # checking if present in cache
        one_uuid = str(self.uuid).upper()
        res_file = os.path.join(CACHE_DIR, one_uuid)

        if reload or not os.path.isfile(res_file):
            # downloading the image to a file
            one_story_imageURL = self.picture_url()
            # print(f"Downloading for {one_uuid} to {res_file}")
            try:
                # Set the timeout for the request
                response = requests.get(one_story_imageURL, timeout=2)
                if response.status_code == 200:
                    # Load image from bytes
                    image_data = response.content
                    with open(res_file, "wb") as fp:
                        fp.write(image_data)
                else:
                    pass
            except requests.exceptions.Timeout:
                pass
            except requests.exceptions.RequestException:
                pass

        if not image_data and os.path.isfile(res_file):
            # print(f"in cache {res_file}")
            # returning file content
            with open(res_file, "rb") as fp:
                image_data = fp.read()

        return image_data

    def picture_url(self):
        one_uuid = str(self.uuid).upper()

        if one_uuid in DB_OFFICIAL:
            locale = list(DB_OFFICIAL[one_uuid]["locales_available"].keys())[0]
            image = DB_OFFICIAL[one_uuid]["localized_infos"][locale].get("image")
            if image:
                url = "https://storage.googleapis.com/lunii-data-prod" + image.get("image_url")
                return url
        return None

    def get_meta(self):
        one_uuid = self.str_uuid

        # checking third-party DB
        if one_uuid in DB_THIRD_PARTY:
            meta = DB_THIRD_PARTY[one_uuid]
            return json.dumps(meta)

        return None

    def night_mode(self):
        return self.nm

    def is_official(self):
        global DB_OFFICIAL
        return str(self.uuid).upper() in DB_OFFICIAL


class StoryList(List[Story]):
    def __init__(self):
        super().__init__()

    def __contains__(self, key_part):
        for one_story in self:
            if _uuid_match(one_story.uuid, str(key_part)):
                return True
        return False

    def get_story(self, key_part: str):
        for one_story in self:
            if _uuid_match(one_story.uuid, str(key_part)):
                return one_story

    def matching_stories(self, short_uuid):
        slist = [one_story for one_story in self if _uuid_match(one_story.uuid, short_uuid)]
        return slist


def story_is_studio(contents):
    file: str
    for file in contents:
        for studio_pattern in [FILE_STUDIO_JSON, FILE_STUDIO_THUMB, "assets/"]:
            if studio_pattern in file:
                return True

    return False

def story_is_plain(contents):
    return all(any(file.lower().endswith(pattern) for file in contents) for pattern in [FILE_UUID])

def story_is_flam(contents):
    return all(any(file.lower().endswith(pattern) for file in contents) for pattern in [".lsf"])

def story_is_flam_plain(contents):
    return all(any(file.lower().endswith(pattern) for file in contents) for pattern in [".lua"])


def story_is_lunii(contents):
    return all(any(file.lower().endswith(pattern) for file in contents) for pattern in ["ri", "si", "li", "ni"])

def story_is_lunii_plain(contents):
    return all(any(file.lower().endswith(pattern) for file in contents) for pattern in ["ri.plain", "si.plain", "li.plain"])
