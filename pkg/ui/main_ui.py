# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListView, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSplitter, QStatusBar,
    QTabWidget, QTextBrowser, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(917, 589)
        MainWindow.setMinimumSize(QSize(500, 0))
        icon = QIcon()
        icon.addFile(u":/icon/res/lunii.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(u"Ctrl+Q")
#endif // QT_CONFIG(shortcut)
        self.actionExit.setMenuRole(QAction.MenuRole.QuitRole)
        self.actionExit.setShortcutVisibleInContextMenu(True)
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        icon1 = QIcon()
        icon1.addFile(u":/icon/res/import.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionImport.setIcon(icon1)
#if QT_CONFIG(shortcut)
        self.actionImport.setShortcut(u"Ctrl+I")
#endif // QT_CONFIG(shortcut)
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        icon2 = QIcon()
        icon2.addFile(u":/icon/res/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExport.setIcon(icon2)
#if QT_CONFIG(shortcut)
        self.actionExport.setShortcut(u"Ctrl+S")
#endif // QT_CONFIG(shortcut)
        self.actionExport_All = QAction(MainWindow)
        self.actionExport_All.setObjectName(u"actionExport_All")
        self.actionExport_All.setIcon(icon2)
#if QT_CONFIG(shortcut)
        self.actionExport_All.setShortcut(u"Ctrl+Shift+S")
#endif // QT_CONFIG(shortcut)
        self.actionMove_Up = QAction(MainWindow)
        self.actionMove_Up.setObjectName(u"actionMove_Up")
        icon3 = QIcon()
        icon3.addFile(u":/icon/res/up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMove_Up.setIcon(icon3)
#if QT_CONFIG(shortcut)
        self.actionMove_Up.setShortcut(u"Alt+Up")
#endif // QT_CONFIG(shortcut)
        self.actionMove_Down = QAction(MainWindow)
        self.actionMove_Down.setObjectName(u"actionMove_Down")
        icon4 = QIcon()
        icon4.addFile(u":/icon/res/down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMove_Down.setIcon(icon4)
#if QT_CONFIG(shortcut)
        self.actionMove_Down.setShortcut(u"Alt+Down")
#endif // QT_CONFIG(shortcut)
        self.actionRemove = QAction(MainWindow)
        self.actionRemove.setObjectName(u"actionRemove")
        icon5 = QIcon()
        icon5.addFile(u":/icon/res/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRemove.setIcon(icon5)
#if QT_CONFIG(shortcut)
        self.actionRemove.setShortcut(u"Del")
#endif // QT_CONFIG(shortcut)
        self.actionShow_size = QAction(MainWindow)
        self.actionShow_size.setObjectName(u"actionShow_size")
        self.actionShow_size.setCheckable(True)
        self.actionShow_size.setChecked(True)
        self.actionShow_size.setEnabled(True)
        self.actionGet_firmware = QAction(MainWindow)
        self.actionGet_firmware.setObjectName(u"actionGet_firmware")
        self.actionGet_firmware.setEnabled(False)
        icon6 = QIcon()
        icon6.addFile(u":/icon/res/fw.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionGet_firmware.setIcon(icon6)
        self.actionShow_unavailable = QAction(MainWindow)
        self.actionShow_unavailable.setObjectName(u"actionShow_unavailable")
        self.actionShow_unavailable.setCheckable(True)
        self.actionShow_unavailable.setChecked(True)
        self.actionMove_Top = QAction(MainWindow)
        self.actionMove_Top.setObjectName(u"actionMove_Top")
        icon7 = QIcon()
        icon7.addFile(u":/icon/res/top.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMove_Top.setIcon(icon7)
#if QT_CONFIG(shortcut)
        self.actionMove_Top.setShortcut(u"Ctrl+Up")
#endif // QT_CONFIG(shortcut)
        self.actionMove_Bottom = QAction(MainWindow)
        self.actionMove_Bottom.setObjectName(u"actionMove_Bottom")
        icon8 = QIcon()
        icon8.addFile(u":/icon/res/bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMove_Bottom.setIcon(icon8)
#if QT_CONFIG(shortcut)
        self.actionMove_Bottom.setShortcut(u"Ctrl+Down")
#endif // QT_CONFIG(shortcut)
        self.actionOpen_Lunii = QAction(MainWindow)
        self.actionOpen_Lunii.setObjectName(u"actionOpen_Lunii")
        icon9 = QIcon()
        icon9.addFile(u":/icon/res/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen_Lunii.setIcon(icon9)
#if QT_CONFIG(shortcut)
        self.actionOpen_Lunii.setShortcut(u"Ctrl+O")
#endif // QT_CONFIG(shortcut)
        self.actionOpen_Lunii.setShortcutVisibleInContextMenu(True)
        self.actionShow_Log = QAction(MainWindow)
        self.actionShow_Log.setObjectName(u"actionShow_Log")
        icon10 = QIcon()
        icon10.addFile(u":/icon/res/debug_log.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionShow_Log.setIcon(icon10)
#if QT_CONFIG(shortcut)
        self.actionShow_Log.setShortcut(u"Ctrl+L")
#endif // QT_CONFIG(shortcut)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon11 = QIcon()
        icon11.addFile(u":/icon/res/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon11)
        self.actionAbout.setMenuRole(QAction.MenuRole.AboutRole)
        self.actionUpdate = QAction(MainWindow)
        self.actionUpdate.setObjectName(u"actionUpdate")
        self.actionUpdate.setIcon(icon6)
        self.actionTranscode = QAction(MainWindow)
        self.actionTranscode.setObjectName(u"actionTranscode")
        self.actionTranscode.setCheckable(True)
        self.actionTranscode.setChecked(True)
        self.actionTranscode.setEnabled(False)
        self.actionRecover_stories = QAction(MainWindow)
        self.actionRecover_stories.setObjectName(u"actionRecover_stories")
        self.actionRemove_stories = QAction(MainWindow)
        self.actionRemove_stories.setObjectName(u"actionRemove_stories")
        self.actionFactory_reset = QAction(MainWindow)
        self.actionFactory_reset.setObjectName(u"actionFactory_reset")
        icon12 = QIcon(QIcon.fromTheme(u"dialog-warning"))
        self.actionFactory_reset.setIcon(icon12)
        self.actionFind_stories = QAction(MainWindow)
        self.actionFind_stories.setObjectName(u"actionFind_stories")
        self.actionHide = QAction(MainWindow)
        self.actionHide.setObjectName(u"actionHide")
#if QT_CONFIG(shortcut)
        self.actionHide.setShortcut(u"Ctrl+H")
#endif // QT_CONFIG(shortcut)
        self.actionImport_DB = QAction(MainWindow)
        self.actionImport_DB.setObjectName(u"actionImport_DB")
        self.actionImport_DB.setIcon(icon1)
        self.actionRefresh_DB = QAction(MainWindow)
        self.actionRefresh_DB.setObjectName(u"actionRefresh_DB")
        icon13 = QIcon()
        icon13.addFile(u":/icon/res/refresh_db.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRefresh_DB.setIcon(icon13)
        self.actionNight_Mode = QAction(MainWindow)
        self.actionNight_Mode.setObjectName(u"actionNight_Mode")
#if QT_CONFIG(shortcut)
        self.actionNight_Mode.setShortcut(u"Ctrl+N")
#endif // QT_CONFIG(shortcut)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_layout = QHBoxLayout()
        self.top_layout.setSpacing(6)
        self.top_layout.setObjectName(u"top_layout")
        self.btn_refresh = QPushButton(self.centralwidget)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(9)
        self.btn_refresh.setFont(font)
        icon14 = QIcon()
        icon14.addFile(u":/icon/res/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh.setIcon(icon14)
        self.btn_refresh.setIconSize(QSize(22, 22))
        self.btn_refresh.setFlat(True)

        self.top_layout.addWidget(self.btn_refresh)

        self.combo_device = QComboBox(self.centralwidget)
        self.combo_device.addItem(u"D:\\")
        self.combo_device.addItem(u"F:\\")
        self.combo_device.setObjectName(u"combo_device")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_device.sizePolicy().hasHeightForWidth())
        self.combo_device.setSizePolicy(sizePolicy)
        self.combo_device.setMaximumSize(QSize(200, 16777215))
        self.combo_device.setEditable(False)

        self.top_layout.addWidget(self.combo_device)

        self.btn_nightmode = QPushButton(self.centralwidget)
        self.btn_nightmode.setObjectName(u"btn_nightmode")
        self.btn_nightmode.setEnabled(False)
        self.btn_nightmode.setMaximumSize(QSize(55, 25))
        self.btn_nightmode.setText(u"")
        icon15 = QIcon()
        icon15.addFile(u":/icon/res/mode_day.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_nightmode.setIcon(icon15)
        self.btn_nightmode.setIconSize(QSize(150, 22))
        self.btn_nightmode.setFlat(True)

        self.top_layout.addWidget(self.btn_nightmode)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.top_layout.addItem(self.horizontalSpacer)

        self.le_filter = QLineEdit(self.centralwidget)
        self.le_filter.setObjectName(u"le_filter")
        self.le_filter.setClearButtonEnabled(True)

        self.top_layout.addWidget(self.le_filter)

        self.btn_db = QPushButton(self.centralwidget)
        self.btn_db.setObjectName(u"btn_db")
        self.btn_db.setMaximumSize(QSize(25, 25))
        self.btn_db.setIcon(icon13)
        self.btn_db.setIconSize(QSize(22, 22))
        self.btn_db.setFlat(True)

        self.top_layout.addWidget(self.btn_db)


        self.verticalLayout_2.addLayout(self.top_layout)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabLuniiContent = QWidget()
        self.tabLuniiContent.setObjectName(u"tabLuniiContent")
        sizePolicy1.setHeightForWidth(self.tabLuniiContent.sizePolicy().hasHeightForWidth())
        self.tabLuniiContent.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.tabLuniiContent)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.tree_stories = QTreeWidget(self.tabLuniiContent)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(4, Qt.AlignLeading|Qt.AlignVCenter);
        __qtreewidgetitem.setText(3, u"UUID");
        __qtreewidgetitem.setText(2, u"DB");
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem.setText(1, u"NM");
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        self.tree_stories.setHeaderItem(__qtreewidgetitem)
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        __qtreewidgetitem1 = QTreeWidgetItem(self.tree_stories)
        __qtreewidgetitem1.setText(4, u"75MB");
        __qtreewidgetitem1.setText(3, u"C4139D59-872A-4D15-8CF1-76D34CDF38C6");
        __qtreewidgetitem1.setFont(3, font1);
        __qtreewidgetitem1.setText(2, u"O");
        __qtreewidgetitem1.setText(0, u"Suzanne et Gaston");
        __qtreewidgetitem2 = QTreeWidgetItem(self.tree_stories)
        __qtreewidgetitem2.setText(4, u"25MB");
        __qtreewidgetitem2.setText(3, u"29264ADF-5A9F-451A-B1EC-2AE21BBA473C");
        __qtreewidgetitem2.setText(2, u"C");
        __qtreewidgetitem2.setText(0, u"Sur les bancs de l'\u00e9cole");
        __qtreewidgetitem3 = QTreeWidgetItem(self.tree_stories)
        __qtreewidgetitem3.setText(4, u"65MB");
        __qtreewidgetitem3.setText(3, u"03933BA4-4FBF-475F-9ECC-35EFB4D11DC9");
        __qtreewidgetitem3.setFont(3, font1);
        __qtreewidgetitem3.setText(2, u"O");
        __qtreewidgetitem3.setText(1, u"z");
        __qtreewidgetitem3.setText(0, u"Panique aux 6 Royaumes");
        __qtreewidgetitem4 = QTreeWidgetItem(self.tree_stories)
        __qtreewidgetitem4.setText(4, u"124MB");
        __qtreewidgetitem4.setText(3, u"22137B29-8646-4335-8069-4A4C9A2D7E89");
        __qtreewidgetitem4.setText(2, u"O");
        __qtreewidgetitem4.setText(0, u"Au Pays des Loups");
        self.tree_stories.setObjectName(u"tree_stories")
        self.tree_stories.setMinimumSize(QSize(0, 150))
        self.tree_stories.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tree_stories.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tree_stories.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_stories.setDragEnabled(True)
        self.tree_stories.setDragDropMode(QAbstractItemView.DragDropMode.DropOnly)
        self.tree_stories.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.tree_stories.setAlternatingRowColors(True)
        self.tree_stories.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tree_stories.setIndentation(20)
        self.tree_stories.setRootIsDecorated(True)
        self.tree_stories.setItemsExpandable(True)
        self.tree_stories.setSortingEnabled(False)
        self.tree_stories.setAllColumnsShowFocus(True)
        self.tree_stories.header().setStretchLastSection(False)

        self.verticalLayout_3.addWidget(self.tree_stories)

        self.tabWidget.addTab(self.tabLuniiContent, "")
        self.tabOfficialStories = QWidget()
        self.tabOfficialStories.setObjectName(u"tabOfficialStories")
        self.tabOfficialStories.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.tabOfficialStories.sizePolicy().hasHeightForWidth())
        self.tabOfficialStories.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.tabOfficialStories)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.local_db_layout = QHBoxLayout()
        self.local_db_layout.setSpacing(2)
        self.local_db_layout.setObjectName(u"local_db_layout")
        self.radio_official_table = QRadioButton(self.tabOfficialStories)
        self.radio_official_table.setObjectName(u"radio_official_table")
        self.radio_official_table.setChecked(True)

        self.local_db_layout.addWidget(self.radio_official_table)

        self.radio_official_gallery = QRadioButton(self.tabOfficialStories)
        self.radio_official_gallery.setObjectName(u"radio_official_gallery")
        self.radio_official_gallery.setChecked(False)

        self.local_db_layout.addWidget(self.radio_official_gallery)

        self.local_db_line_edit = QLineEdit(self.tabOfficialStories)
        self.local_db_line_edit.setObjectName(u"local_db_line_edit")
        sizePolicy.setHeightForWidth(self.local_db_line_edit.sizePolicy().hasHeightForWidth())
        self.local_db_line_edit.setSizePolicy(sizePolicy)

        self.local_db_layout.addWidget(self.local_db_line_edit)

        self.local_db_choose_folder_button = QPushButton(self.tabOfficialStories)
        self.local_db_choose_folder_button.setObjectName(u"local_db_choose_folder_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.local_db_choose_folder_button.sizePolicy().hasHeightForWidth())
        self.local_db_choose_folder_button.setSizePolicy(sizePolicy2)
        self.local_db_choose_folder_button.setMinimumSize(QSize(25, 25))
        self.local_db_choose_folder_button.setMaximumSize(QSize(25, 25))

        self.local_db_layout.addWidget(self.local_db_choose_folder_button)


        self.verticalLayout.addLayout(self.local_db_layout)

        self.list_stories_official = QListView(self.tabOfficialStories)
        self.list_stories_official.setObjectName(u"list_stories_official")
        self.list_stories_official.setEnabled(True)
        self.list_stories_official.setMinimumSize(QSize(600, 200))
        self.list_stories_official.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list_stories_official.setProperty("showDropIndicator", False)
        self.list_stories_official.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.list_stories_official.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.list_stories_official.setWordWrap(True)

        self.verticalLayout.addWidget(self.list_stories_official)

        self.tree_stories_official = QTreeWidget(self.tabOfficialStories)
        __qtreewidgetitem5 = QTreeWidgetItem()
        __qtreewidgetitem5.setText(5, u"UUID");
        __qtreewidgetitem5.setTextAlignment(2, Qt.AlignLeading|Qt.AlignVCenter);
        __qtreewidgetitem5.setTextAlignment(0, Qt.AlignLeading|Qt.AlignVCenter);
        self.tree_stories_official.setHeaderItem(__qtreewidgetitem5)
        self.tree_stories_official.setObjectName(u"tree_stories_official")
        sizePolicy1.setHeightForWidth(self.tree_stories_official.sizePolicy().hasHeightForWidth())
        self.tree_stories_official.setSizePolicy(sizePolicy1)
        self.tree_stories_official.setMinimumSize(QSize(600, 200))
        self.tree_stories_official.setFrameShape(QFrame.Shape.NoFrame)
        self.tree_stories_official.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tree_stories_official.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tree_stories_official.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_stories_official.setProperty("showDropIndicator", False)
        self.tree_stories_official.setDragEnabled(False)
        self.tree_stories_official.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.tree_stories_official.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.tree_stories_official.setAlternatingRowColors(True)
        self.tree_stories_official.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tree_stories_official.setIndentation(20)
        self.tree_stories_official.setRootIsDecorated(True)
        self.tree_stories_official.setItemsExpandable(True)
        self.tree_stories_official.setSortingEnabled(True)
        self.tree_stories_official.setAllColumnsShowFocus(True)
        self.tree_stories_official.setExpandsOnDoubleClick(True)
        self.tree_stories_official.header().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tree_stories_official)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tabOfficialStories, "")
        self.tabThirdPartyStories = QWidget()
        self.tabThirdPartyStories.setObjectName(u"tabThirdPartyStories")
        self.verticalLayout_5 = QVBoxLayout(self.tabThirdPartyStories)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.third_party_db_layout = QHBoxLayout()
        self.third_party_db_layout.setSpacing(2)
        self.third_party_db_layout.setObjectName(u"third_party_db_layout")
        self.radio_third_party_table = QRadioButton(self.tabThirdPartyStories)
        self.radio_third_party_table.setObjectName(u"radio_third_party_table")
        self.radio_third_party_table.setChecked(True)

        self.third_party_db_layout.addWidget(self.radio_third_party_table)

        self.radio_third_party_gallery = QRadioButton(self.tabThirdPartyStories)
        self.radio_third_party_gallery.setObjectName(u"radio_third_party_gallery")
        self.radio_third_party_gallery.setChecked(False)

        self.third_party_db_layout.addWidget(self.radio_third_party_gallery)

        self.third_party_db_line_edit = QLineEdit(self.tabThirdPartyStories)
        self.third_party_db_line_edit.setObjectName(u"third_party_db_line_edit")
        sizePolicy.setHeightForWidth(self.third_party_db_line_edit.sizePolicy().hasHeightForWidth())
        self.third_party_db_line_edit.setSizePolicy(sizePolicy)

        self.third_party_db_layout.addWidget(self.third_party_db_line_edit)

        self.third_party_db_choose_folder_button = QPushButton(self.tabThirdPartyStories)
        self.third_party_db_choose_folder_button.setObjectName(u"third_party_db_choose_folder_button")
        sizePolicy2.setHeightForWidth(self.third_party_db_choose_folder_button.sizePolicy().hasHeightForWidth())
        self.third_party_db_choose_folder_button.setSizePolicy(sizePolicy2)
        self.third_party_db_choose_folder_button.setMinimumSize(QSize(25, 25))
        self.third_party_db_choose_folder_button.setMaximumSize(QSize(25, 25))

        self.third_party_db_layout.addWidget(self.third_party_db_choose_folder_button)


        self.verticalLayout_5.addLayout(self.third_party_db_layout)

        self.list_stories_third_party = QListView(self.tabThirdPartyStories)
        self.list_stories_third_party.setObjectName(u"list_stories_third_party")
        self.list_stories_third_party.setEnabled(True)
        self.list_stories_third_party.setMinimumSize(QSize(600, 200))
        self.list_stories_third_party.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.list_stories_third_party.setProperty("showDropIndicator", False)
        self.list_stories_third_party.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.list_stories_third_party.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.list_stories_third_party.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.list_stories_third_party)

        self.tree_stories_third_party = QTreeWidget(self.tabThirdPartyStories)
        __qtreewidgetitem6 = QTreeWidgetItem()
        __qtreewidgetitem6.setText(4, u"UUID");
        __qtreewidgetitem6.setTextAlignment(0, Qt.AlignLeading|Qt.AlignVCenter);
        self.tree_stories_third_party.setHeaderItem(__qtreewidgetitem6)
        self.tree_stories_third_party.setObjectName(u"tree_stories_third_party")
        sizePolicy1.setHeightForWidth(self.tree_stories_third_party.sizePolicy().hasHeightForWidth())
        self.tree_stories_third_party.setSizePolicy(sizePolicy1)
        self.tree_stories_third_party.setMinimumSize(QSize(600, 200))
        self.tree_stories_third_party.setFrameShape(QFrame.Shape.NoFrame)
        self.tree_stories_third_party.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tree_stories_third_party.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tree_stories_third_party.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_stories_third_party.setProperty("showDropIndicator", False)
        self.tree_stories_third_party.setDragEnabled(False)
        self.tree_stories_third_party.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.tree_stories_third_party.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.tree_stories_third_party.setAlternatingRowColors(True)
        self.tree_stories_third_party.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tree_stories_third_party.setIndentation(20)
        self.tree_stories_third_party.setRootIsDecorated(True)
        self.tree_stories_third_party.setItemsExpandable(True)
        self.tree_stories_third_party.setSortingEnabled(True)
        self.tree_stories_third_party.setAllColumnsShowFocus(True)
        self.tree_stories_third_party.setExpandsOnDoubleClick(True)
        self.tree_stories_third_party.header().setStretchLastSection(False)

        self.verticalLayout_5.addWidget(self.tree_stories_third_party)

        self.tabWidget.addTab(self.tabThirdPartyStories, "")
        self.splitter.addWidget(self.tabWidget)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        sizePolicy1.setHeightForWidth(self.layoutWidget.sizePolicy().hasHeightForWidth())
        self.layoutWidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.story_details = QTextBrowser(self.layoutWidget)
        self.story_details.setObjectName(u"story_details")
        sizePolicy1.setHeightForWidth(self.story_details.sizePolicy().hasHeightForWidth())
        self.story_details.setSizePolicy(sizePolicy1)
        self.story_details.setMinimumSize(QSize(300, 192))
        self.story_details.setMaximumSize(QSize(16777215, 16777215))
        self.story_details.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.story_details.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)

        self.verticalLayout_6.addWidget(self.story_details)

        self.horizontalLayout5 = QHBoxLayout()
        self.horizontalLayout5.setObjectName(u"horizontalLayout5")
        self.add_story_button = QPushButton(self.layoutWidget)
        self.add_story_button.setObjectName(u"add_story_button")

        self.horizontalLayout5.addWidget(self.add_story_button)

        self.remove_story_button = QPushButton(self.layoutWidget)
        self.remove_story_button.setObjectName(u"remove_story_button")

        self.horizontalLayout5.addWidget(self.remove_story_button)


        self.verticalLayout_6.addLayout(self.horizontalLayout5)

        self.prognstopLayout = QHBoxLayout()
        self.prognstopLayout.setObjectName(u"prognstopLayout")
        self.progressLayout = QVBoxLayout()
        self.progressLayout.setSpacing(0)
        self.progressLayout.setObjectName(u"progressLayout")
        self.totalLayout = QHBoxLayout()
        self.totalLayout.setSpacing(6)
        self.totalLayout.setObjectName(u"totalLayout")
        self.lbl_total = QLabel(self.layoutWidget)
        self.lbl_total.setObjectName(u"lbl_total")
        self.lbl_total.setMinimumSize(QSize(80, 0))
        self.lbl_total.setFrameShape(QFrame.Shape.Panel)
        self.lbl_total.setFrameShadow(QFrame.Shadow.Sunken)
        self.lbl_total.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.totalLayout.addWidget(self.lbl_total)

        self.pbar_total = QProgressBar(self.layoutWidget)
        self.pbar_total.setObjectName(u"pbar_total")
        self.pbar_total.setMaximumSize(QSize(16777215, 10))
        self.pbar_total.setValue(24)
        self.pbar_total.setTextVisible(False)

        self.totalLayout.addWidget(self.pbar_total)


        self.progressLayout.addLayout(self.totalLayout)

        self.storyLayout = QHBoxLayout()
        self.storyLayout.setSpacing(6)
        self.storyLayout.setObjectName(u"storyLayout")
        self.lbl_story = QLabel(self.layoutWidget)
        self.lbl_story.setObjectName(u"lbl_story")
        self.lbl_story.setMinimumSize(QSize(80, 0))
        self.lbl_story.setFrameShape(QFrame.Shape.Panel)
        self.lbl_story.setFrameShadow(QFrame.Shadow.Sunken)
        self.lbl_story.setText(u"8B_UUID")
        self.lbl_story.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.storyLayout.addWidget(self.lbl_story)

        self.pbar_story = QProgressBar(self.layoutWidget)
        self.pbar_story.setObjectName(u"pbar_story")
        self.pbar_story.setMaximumSize(QSize(16777215, 10))
        self.pbar_story.setValue(24)
        self.pbar_story.setTextVisible(False)

        self.storyLayout.addWidget(self.pbar_story)


        self.progressLayout.addLayout(self.storyLayout)


        self.prognstopLayout.addLayout(self.progressLayout)

        self.btn_abort = QPushButton(self.layoutWidget)
        self.btn_abort.setObjectName(u"btn_abort")
        self.btn_abort.setIcon(icon5)
        self.btn_abort.setIconSize(QSize(24, 24))

        self.prognstopLayout.addWidget(self.btn_abort)


        self.verticalLayout_6.addLayout(self.prognstopLayout)

        self.splitter.addWidget(self.layoutWidget)

        self.verticalLayout_2.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QRect(0, 0, 917, 21))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setSeparatorsCollapsible(True)
        self.menuFile.setToolTipsVisible(False)
        self.menuTools = QMenu(self.menuBar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuLost_stories = QMenu(self.menuTools)
        self.menuLost_stories.setObjectName(u"menuLost_stories")
        self.menuStory = QMenu(self.menuBar)
        self.menuStory.setObjectName(u"menuStory")
        self.menuUpdate = QMenu(self.menuBar)
        self.menuUpdate.setObjectName(u"menuUpdate")
        self.menuUpdate.setEnabled(False)
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.combo_device, self.le_filter)
        QWidget.setTabOrder(self.le_filter, self.tree_stories)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuStory.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuBar.addAction(self.menuUpdate.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_Lunii)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport_DB)
        self.menuFile.addAction(self.actionRefresh_DB)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionShow_size)
        self.menuTools.addAction(self.actionShow_unavailable)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionShow_Log)
        self.menuTools.addAction(self.actionGet_firmware)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.menuLost_stories.menuAction())
        self.menuTools.addAction(self.actionFactory_reset)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionTranscode)
        self.menuLost_stories.addAction(self.actionFind_stories)
        self.menuLost_stories.addAction(self.actionRecover_stories)
        self.menuLost_stories.addAction(self.actionRemove_stories)
        self.menuStory.addAction(self.actionMove_Top)
        self.menuStory.addAction(self.actionMove_Up)
        self.menuStory.addAction(self.actionMove_Down)
        self.menuStory.addAction(self.actionMove_Bottom)
        self.menuStory.addSeparator()
        self.menuStory.addAction(self.actionHide)
        self.menuStory.addAction(self.actionNight_Mode)
        self.menuStory.addSeparator()
        self.menuStory.addAction(self.actionImport)
        self.menuStory.addAction(self.actionExport)
        self.menuStory.addAction(self.actionExport_All)
        self.menuStory.addAction(self.actionRemove)
        self.menuHelp.addAction(self.actionUpdate)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        self.combo_device.currentIndexChanged.connect(self.tree_stories.clear)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lunii Qt-Manager", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionExport_All.setText(QCoreApplication.translate("MainWindow", u"Export All", None))
        self.actionMove_Up.setText(QCoreApplication.translate("MainWindow", u"Move Up", None))
        self.actionMove_Down.setText(QCoreApplication.translate("MainWindow", u"Move Down", None))
        self.actionRemove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.actionShow_size.setText(QCoreApplication.translate("MainWindow", u"Show size", None))
#if QT_CONFIG(tooltip)
        self.actionShow_size.setToolTip(QCoreApplication.translate("MainWindow", u"Show size for each stories", None))
#endif // QT_CONFIG(tooltip)
        self.actionGet_firmware.setText(QCoreApplication.translate("MainWindow", u"Get FW Update", None))
#if QT_CONFIG(tooltip)
        self.actionGet_firmware.setToolTip(QCoreApplication.translate("MainWindow", u"Get firmaware update for current Lunii", None))
#endif // QT_CONFIG(tooltip)
        self.actionShow_unavailable.setText(QCoreApplication.translate("MainWindow", u"Show unavailable stories", None))
#if QT_CONFIG(tooltip)
        self.actionShow_unavailable.setToolTip(QCoreApplication.translate("MainWindow", u"Show unavailable stories", None))
#endif // QT_CONFIG(tooltip)
        self.actionMove_Top.setText(QCoreApplication.translate("MainWindow", u"Move Top", None))
        self.actionMove_Bottom.setText(QCoreApplication.translate("MainWindow", u"Move Bottom", None))
        self.actionOpen_Lunii.setText(QCoreApplication.translate("MainWindow", u"Open device", None))
#if QT_CONFIG(tooltip)
        self.actionOpen_Lunii.setToolTip(QCoreApplication.translate("MainWindow", u"Open Lunii or Flam device", None))
#endif // QT_CONFIG(tooltip)
        self.actionShow_Log.setText(QCoreApplication.translate("MainWindow", u"Show Log", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionUpdate.setText(QCoreApplication.translate("MainWindow", u"Update to v2.X.X", None))
        self.actionTranscode.setText(QCoreApplication.translate("MainWindow", u"FFMPEG detected", None))
        self.actionRecover_stories.setText(QCoreApplication.translate("MainWindow", u"Recover", None))
        self.actionRemove_stories.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.actionFactory_reset.setText(QCoreApplication.translate("MainWindow", u"Factory Reset", None))
        self.actionFind_stories.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.actionHide.setText(QCoreApplication.translate("MainWindow", u"Hide / Show", None))
        self.actionImport_DB.setText(QCoreApplication.translate("MainWindow", u"Import STUdio DB", None))
        self.actionRefresh_DB.setText(QCoreApplication.translate("MainWindow", u"Refresh official DB", None))
        self.actionNight_Mode.setText(QCoreApplication.translate("MainWindow", u"Force Night Mode", None))
#if QT_CONFIG(tooltip)
        self.btn_refresh.setToolTip(QCoreApplication.translate("MainWindow", u"Refresh connected devices", None))
#endif // QT_CONFIG(tooltip)
        self.btn_refresh.setText("")

#if QT_CONFIG(tooltip)
        self.combo_device.setToolTip(QCoreApplication.translate("MainWindow", u"Select your Lunii", None))
#endif // QT_CONFIG(tooltip)
        self.combo_device.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select your Lunii", None))
        self.le_filter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Story Name or UUID filter text)", None))
#if QT_CONFIG(tooltip)
        self.btn_db.setToolTip(QCoreApplication.translate("MainWindow", u"Force official Lunii DB to be refreshed", None))
#endif // QT_CONFIG(tooltip)
        self.btn_db.setText("")
        ___qtreewidgetitem = self.tree_stories.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Story Name", None));
#if QT_CONFIG(tooltip)
        ___qtreewidgetitem.setToolTip(2, QCoreApplication.translate("MainWindow", u"Database source (Official / Third Party)", None));
        ___qtreewidgetitem.setToolTip(1, QCoreApplication.translate("MainWindow", u"Night Mode", None));
#endif // QT_CONFIG(tooltip)

        __sortingEnabled = self.tree_stories.isSortingEnabled()
        self.tree_stories.setSortingEnabled(False)
        self.tree_stories.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLuniiContent), QCoreApplication.translate("MainWindow", u"My Lunii", None))
        self.radio_official_table.setText(QCoreApplication.translate("MainWindow", u"List", None))
        self.radio_official_gallery.setText(QCoreApplication.translate("MainWindow", u"Gallery", None))
        self.local_db_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Local Story Library path)", None))
        self.local_db_choose_folder_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        ___qtreewidgetitem1 = self.tree_stories_official.headerItem()
        ___qtreewidgetitem1.setText(6, QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"Path", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Installation Id", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Language", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Story Name", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Age", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOfficialStories), QCoreApplication.translate("MainWindow", u"Official Store", None))
        self.radio_third_party_table.setText(QCoreApplication.translate("MainWindow", u"List", None))
        self.radio_third_party_gallery.setText(QCoreApplication.translate("MainWindow", u"Gallery", None))
        self.third_party_db_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Third Party Story Library path)", None))
        self.third_party_db_choose_folder_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        ___qtreewidgetitem2 = self.tree_stories_third_party.headerItem()
        ___qtreewidgetitem2.setText(5, QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtreewidgetitem2.setText(3, QCoreApplication.translate("MainWindow", u"Path", None));
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"Installation Id", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"Story Name", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Age", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabThirdPartyStories), QCoreApplication.translate("MainWindow", u"Third Party Store", None))
        self.add_story_button.setText(QCoreApplication.translate("MainWindow", u"Add Story", None))
        self.remove_story_button.setText(QCoreApplication.translate("MainWindow", u"Remove Story", None))
        self.lbl_total.setText(QCoreApplication.translate("MainWindow", u"Total", None))
#if QT_CONFIG(tooltip)
        self.btn_abort.setToolTip(QCoreApplication.translate("MainWindow", u"Abort current process", None))
#endif // QT_CONFIG(tooltip)
        self.btn_abort.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"&Tools", None))
        self.menuLost_stories.setTitle(QCoreApplication.translate("MainWindow", u"Lost stories", None))
        self.menuStory.setTitle(QCoreApplication.translate("MainWindow", u"&Stories", None))
        self.menuUpdate.setTitle(QCoreApplication.translate("MainWindow", u"Update 2.2.X is released", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

