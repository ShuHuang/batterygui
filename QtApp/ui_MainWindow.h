/********************************************************************************
** Form generated from reading UI file 'MainWindow.ui'
**
** Created by: Qt User Interface Compiler version 5.10.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QDate>
#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDateEdit>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTableView>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actOpenDB;
    QAction *actQuit;
    QAction *actRecAppend;
    QAction *actRecInsert;
    QAction *actSubmit;
    QAction *actRevert;
    QAction *actRecDelete;
    QAction *actPhoto;
    QAction *actPhotoClear;
    QAction *actScan;
    QWidget *centralWidget;
    QSplitter *splitter;
    QGroupBox *groupBox_3;
    QVBoxLayout *verticalLayout_2;
    QFrame *frame;
    QHBoxLayout *horizontalLayout_2;
    QGroupBox *groupBoxSort;
    QGridLayout *gridLayout_3;
    QLabel *label_14;
    QComboBox *comboFields;
    QSpacerItem *horizontalSpacer;
    QRadioButton *radioBtnAscend;
    QRadioButton *radioBtnDescend;
    QGroupBox *groupBoxFilter;
    QGridLayout *gridLayout_2;
    QRadioButton *radioBtnMan;
    QRadioButton *radioBtnWoman;
    QRadioButton *radioBtnBoth;
    QSpacerItem *horizontalSpacer_2;
    QSpacerItem *horizontalSpacer_3;
    QTableView *tableView;
    QGroupBox *groupBox;
    QHBoxLayout *horizontalLayout;
    QGridLayout *gridLayout;
    QLabel *label_2;
    QComboBox *dbComboSex;
    QLabel *label_3;
    QLineEdit *dbEditName;
    QLabel *label_9;
    QLabel *label_12;
    QSpinBox *dbSpinSalary;
    QPlainTextEdit *dbEditMemo;
    QComboBox *dbComboDep;
    QLabel *label_6;
    QSpinBox *dbSpinEmpNo;
    QLabel *label;
    QLabel *label_7;
    QComboBox *dbComboProvince;
    QLabel *label_5;
    QDateEdit *dbEditBirth;
    QVBoxLayout *verticalLayout;
    QLabel *label_13;
    QLabel *dbLabPhoto;
    QSpacerItem *verticalSpacer;
    QMenuBar *menuBar;
    QStatusBar *statusBar;
    QToolBar *mainToolBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(949, 610);
        QFont font;
        font.setPointSize(11);
        MainWindow->setFont(font);
        actOpenDB = new QAction(MainWindow);
        actOpenDB->setObjectName(QStringLiteral("actOpenDB"));
        QIcon icon;
        icon.addFile(QStringLiteral(":/icons/images/open3.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        actOpenDB->setIcon(icon);
        actQuit = new QAction(MainWindow);
        actQuit->setObjectName(QStringLiteral("actQuit"));
        QIcon icon1;
        icon1.addFile(QStringLiteral(":/icons/images/exit.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        actQuit->setIcon(icon1);
        actRecAppend = new QAction(MainWindow);
        actRecAppend->setObjectName(QStringLiteral("actRecAppend"));
        actRecAppend->setEnabled(false);
        QIcon icon2;
        icon2.addFile(QStringLiteral(":/icons/images/316.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        actRecAppend->setIcon(icon2);
        actRecInsert = new QAction(MainWindow);
        actRecInsert->setObjectName(QStringLiteral("actRecInsert"));
        actRecInsert->setEnabled(false);
        QIcon icon3;
        icon3.addFile(QStringLiteral(":/icons/images/306.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        actRecInsert->setIcon(icon3);
        actSubmit = new QAction(MainWindow);
        actSubmit->setObjectName(QStringLiteral("actSubmit"));
        actSubmit->setEnabled(false);
        QIcon icon4;
        icon4.addFile(QStringLiteral(":/icons/images/save1.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        actSubmit->setIcon(icon4);
        actRevert = new QAction(MainWindow);
        actRevert->setObjectName(QStringLiteral("actRevert"));
        actRevert->setEnabled(false);
        QIcon icon5;
        icon5.addFile(QStringLiteral(":/icons/images/ubdo.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        actRevert->setIcon(icon5);
        actRecDelete = new QAction(MainWindow);
        actRecDelete->setObjectName(QStringLiteral("actRecDelete"));
        actRecDelete->setEnabled(false);
        QIcon icon6;
        icon6.addFile(QStringLiteral(":/icons/images/delete1.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        actRecDelete->setIcon(icon6);
        actPhoto = new QAction(MainWindow);
        actPhoto->setObjectName(QStringLiteral("actPhoto"));
        actPhoto->setEnabled(false);
        QIcon icon7;
        icon7.addFile(QStringLiteral(":/icons/images/00.JPG"), QSize(), QIcon::Normal, QIcon::Off);
        actPhoto->setIcon(icon7);
        actPhotoClear = new QAction(MainWindow);
        actPhotoClear->setObjectName(QStringLiteral("actPhotoClear"));
        actPhotoClear->setEnabled(false);
        QIcon icon8;
        icon8.addFile(QStringLiteral(":/icons/images/103.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        actPhotoClear->setIcon(icon8);
        actScan = new QAction(MainWindow);
        actScan->setObjectName(QStringLiteral("actScan"));
        actScan->setEnabled(false);
        QIcon icon9;
        icon9.addFile(QStringLiteral(":/icons/images/up.bmp"), QSize(), QIcon::Normal, QIcon::Off);
        actScan->setIcon(icon9);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        splitter = new QSplitter(centralWidget);
        splitter->setObjectName(QStringLiteral("splitter"));
        splitter->setGeometry(QRect(0, 40, 881, 445));
        splitter->setOrientation(Qt::Horizontal);
        groupBox_3 = new QGroupBox(splitter);
        groupBox_3->setObjectName(QStringLiteral("groupBox_3"));
        verticalLayout_2 = new QVBoxLayout(groupBox_3);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        frame = new QFrame(groupBox_3);
        frame->setObjectName(QStringLiteral("frame"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        horizontalLayout_2 = new QHBoxLayout(frame);
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        groupBoxSort = new QGroupBox(frame);
        groupBoxSort->setObjectName(QStringLiteral("groupBoxSort"));
        groupBoxSort->setEnabled(false);
        gridLayout_3 = new QGridLayout(groupBoxSort);
        gridLayout_3->setSpacing(6);
        gridLayout_3->setContentsMargins(11, 11, 11, 11);
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));
        label_14 = new QLabel(groupBoxSort);
        label_14->setObjectName(QStringLiteral("label_14"));

        gridLayout_3->addWidget(label_14, 0, 0, 1, 1);

        comboFields = new QComboBox(groupBoxSort);
        comboFields->setObjectName(QStringLiteral("comboFields"));

        gridLayout_3->addWidget(comboFields, 0, 1, 1, 2);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_3->addItem(horizontalSpacer, 1, 0, 1, 1);

        radioBtnAscend = new QRadioButton(groupBoxSort);
        radioBtnAscend->setObjectName(QStringLiteral("radioBtnAscend"));
        radioBtnAscend->setChecked(true);

        gridLayout_3->addWidget(radioBtnAscend, 1, 1, 1, 1);

        radioBtnDescend = new QRadioButton(groupBoxSort);
        radioBtnDescend->setObjectName(QStringLiteral("radioBtnDescend"));

        gridLayout_3->addWidget(radioBtnDescend, 1, 2, 1, 1);


        horizontalLayout_2->addWidget(groupBoxSort);

        groupBoxFilter = new QGroupBox(frame);
        groupBoxFilter->setObjectName(QStringLiteral("groupBoxFilter"));
        groupBoxFilter->setEnabled(false);
        gridLayout_2 = new QGridLayout(groupBoxFilter);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        radioBtnMan = new QRadioButton(groupBoxFilter);
        radioBtnMan->setObjectName(QStringLiteral("radioBtnMan"));

        gridLayout_2->addWidget(radioBtnMan, 0, 0, 1, 1);

        radioBtnWoman = new QRadioButton(groupBoxFilter);
        radioBtnWoman->setObjectName(QStringLiteral("radioBtnWoman"));

        gridLayout_2->addWidget(radioBtnWoman, 0, 1, 1, 1);

        radioBtnBoth = new QRadioButton(groupBoxFilter);
        radioBtnBoth->setObjectName(QStringLiteral("radioBtnBoth"));
        radioBtnBoth->setChecked(true);

        gridLayout_2->addWidget(radioBtnBoth, 1, 0, 1, 1);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer_2, 1, 1, 1, 1);


        horizontalLayout_2->addWidget(groupBoxFilter);

        horizontalSpacer_3 = new QSpacerItem(17, 17, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_3);


        verticalLayout_2->addWidget(frame);

        tableView = new QTableView(groupBox_3);
        tableView->setObjectName(QStringLiteral("tableView"));
        tableView->setEditTriggers(QAbstractItemView::AnyKeyPressed|QAbstractItemView::DoubleClicked|QAbstractItemView::EditKeyPressed|QAbstractItemView::SelectedClicked);
        tableView->horizontalHeader()->setDefaultSectionSize(50);

        verticalLayout_2->addWidget(tableView);

        splitter->addWidget(groupBox_3);
        groupBox = new QGroupBox(splitter);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        horizontalLayout = new QHBoxLayout(groupBox);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        gridLayout = new QGridLayout();
        gridLayout->setSpacing(6);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        gridLayout->setHorizontalSpacing(6);
        gridLayout->setVerticalSpacing(12);
        label_2 = new QLabel(groupBox);
        label_2->setObjectName(QStringLiteral("label_2"));

        gridLayout->addWidget(label_2, 1, 0, 1, 1);

        dbComboSex = new QComboBox(groupBox);
        dbComboSex->addItem(QString());
        dbComboSex->addItem(QString());
        dbComboSex->setObjectName(QStringLiteral("dbComboSex"));

        gridLayout->addWidget(dbComboSex, 2, 1, 1, 1);

        label_3 = new QLabel(groupBox);
        label_3->setObjectName(QStringLiteral("label_3"));

        gridLayout->addWidget(label_3, 2, 0, 1, 1);

        dbEditName = new QLineEdit(groupBox);
        dbEditName->setObjectName(QStringLiteral("dbEditName"));

        gridLayout->addWidget(dbEditName, 1, 1, 1, 1);

        label_9 = new QLabel(groupBox);
        label_9->setObjectName(QStringLiteral("label_9"));

        gridLayout->addWidget(label_9, 7, 0, 1, 1);

        label_12 = new QLabel(groupBox);
        label_12->setObjectName(QStringLiteral("label_12"));

        gridLayout->addWidget(label_12, 6, 0, 1, 1);

        dbSpinSalary = new QSpinBox(groupBox);
        dbSpinSalary->setObjectName(QStringLiteral("dbSpinSalary"));
        dbSpinSalary->setMinimum(1000);
        dbSpinSalary->setMaximum(50000);
        dbSpinSalary->setSingleStep(100);
        dbSpinSalary->setValue(1000);

        gridLayout->addWidget(dbSpinSalary, 6, 1, 1, 1);

        dbEditMemo = new QPlainTextEdit(groupBox);
        dbEditMemo->setObjectName(QStringLiteral("dbEditMemo"));
        dbEditMemo->setMaximumSize(QSize(16777215, 16777215));

        gridLayout->addWidget(dbEditMemo, 7, 1, 1, 1);

        dbComboDep = new QComboBox(groupBox);
        dbComboDep->addItem(QString());
        dbComboDep->addItem(QString());
        dbComboDep->addItem(QString());
        dbComboDep->addItem(QString());
        dbComboDep->setObjectName(QStringLiteral("dbComboDep"));
        dbComboDep->setEditable(true);

        gridLayout->addWidget(dbComboDep, 5, 1, 1, 1);

        label_6 = new QLabel(groupBox);
        label_6->setObjectName(QStringLiteral("label_6"));

        gridLayout->addWidget(label_6, 5, 0, 1, 1);

        dbSpinEmpNo = new QSpinBox(groupBox);
        dbSpinEmpNo->setObjectName(QStringLiteral("dbSpinEmpNo"));
        dbSpinEmpNo->setMinimum(1);
        dbSpinEmpNo->setMaximum(10000);

        gridLayout->addWidget(dbSpinEmpNo, 0, 1, 1, 1);

        label = new QLabel(groupBox);
        label->setObjectName(QStringLiteral("label"));

        gridLayout->addWidget(label, 0, 0, 1, 1);

        label_7 = new QLabel(groupBox);
        label_7->setObjectName(QStringLiteral("label_7"));

        gridLayout->addWidget(label_7, 4, 0, 1, 1);

        dbComboProvince = new QComboBox(groupBox);
        dbComboProvince->addItem(QString());
        dbComboProvince->addItem(QString());
        dbComboProvince->addItem(QString());
        dbComboProvince->addItem(QString());
        dbComboProvince->addItem(QString());
        dbComboProvince->addItem(QString());
        dbComboProvince->addItem(QString());
        dbComboProvince->addItem(QString());
        dbComboProvince->addItem(QString());
        dbComboProvince->addItem(QString());
        dbComboProvince->addItem(QString());
        dbComboProvince->addItem(QString());
        dbComboProvince->addItem(QString());
        dbComboProvince->addItem(QString());
        dbComboProvince->setObjectName(QStringLiteral("dbComboProvince"));
        dbComboProvince->setEditable(true);

        gridLayout->addWidget(dbComboProvince, 4, 1, 1, 1);

        label_5 = new QLabel(groupBox);
        label_5->setObjectName(QStringLiteral("label_5"));

        gridLayout->addWidget(label_5, 3, 0, 1, 1);

        dbEditBirth = new QDateEdit(groupBox);
        dbEditBirth->setObjectName(QStringLiteral("dbEditBirth"));
        dbEditBirth->setCalendarPopup(true);
        dbEditBirth->setDate(QDate(2017, 2, 20));

        gridLayout->addWidget(dbEditBirth, 3, 1, 1, 1);


        horizontalLayout->addLayout(gridLayout);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        label_13 = new QLabel(groupBox);
        label_13->setObjectName(QStringLiteral("label_13"));

        verticalLayout->addWidget(label_13);

        dbLabPhoto = new QLabel(groupBox);
        dbLabPhoto->setObjectName(QStringLiteral("dbLabPhoto"));
        dbLabPhoto->setMinimumSize(QSize(150, 0));
        dbLabPhoto->setMaximumSize(QSize(400, 16777215));

        verticalLayout->addWidget(dbLabPhoto);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer);


        horizontalLayout->addLayout(verticalLayout);

        splitter->addWidget(groupBox);
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 949, 23));
        MainWindow->setMenuBar(menuBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        mainToolBar->setIconSize(QSize(16, 16));
        mainToolBar->setToolButtonStyle(Qt::ToolButtonTextUnderIcon);
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
#ifndef QT_NO_SHORTCUT
        label_2->setBuddy(dbEditName);
        label_3->setBuddy(dbComboSex);
        label_9->setBuddy(dbEditMemo);
        label_12->setBuddy(dbSpinSalary);
        label_6->setBuddy(dbComboDep);
        label->setBuddy(dbSpinEmpNo);
        label_7->setBuddy(dbComboProvince);
        label_5->setBuddy(dbEditBirth);
#endif // QT_NO_SHORTCUT

        mainToolBar->addAction(actOpenDB);
        mainToolBar->addSeparator();
        mainToolBar->addAction(actRecAppend);
        mainToolBar->addAction(actRecInsert);
        mainToolBar->addAction(actRecDelete);
        mainToolBar->addSeparator();
        mainToolBar->addAction(actPhoto);
        mainToolBar->addAction(actPhotoClear);
        mainToolBar->addAction(actScan);
        mainToolBar->addSeparator();
        mainToolBar->addAction(actSubmit);
        mainToolBar->addAction(actRevert);
        mainToolBar->addSeparator();
        mainToolBar->addAction(actQuit);

        retranslateUi(MainWindow);
        QObject::connect(actQuit, SIGNAL(triggered()), MainWindow, SLOT(close()));

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Demo7_1, QSqlTableModel\347\232\204\344\275\277\347\224\250", nullptr));
        actOpenDB->setText(QApplication::translate("MainWindow", "\346\211\223\345\274\200", nullptr));
#ifndef QT_NO_TOOLTIP
        actOpenDB->setToolTip(QApplication::translate("MainWindow", "\346\211\223\345\274\200\346\225\260\346\215\256\345\272\223", nullptr));
#endif // QT_NO_TOOLTIP
        actQuit->setText(QApplication::translate("MainWindow", "\351\200\200\345\207\272", nullptr));
#ifndef QT_NO_TOOLTIP
        actQuit->setToolTip(QApplication::translate("MainWindow", "\351\200\200\345\207\272", nullptr));
#endif // QT_NO_TOOLTIP
        actRecAppend->setText(QApplication::translate("MainWindow", "\346\267\273\345\212\240", nullptr));
#ifndef QT_NO_TOOLTIP
        actRecAppend->setToolTip(QApplication::translate("MainWindow", "\346\267\273\345\212\240\350\256\260\345\275\225", nullptr));
#endif // QT_NO_TOOLTIP
        actRecInsert->setText(QApplication::translate("MainWindow", "\346\217\222\345\205\245", nullptr));
#ifndef QT_NO_TOOLTIP
        actRecInsert->setToolTip(QApplication::translate("MainWindow", "\346\217\222\345\205\245\350\256\260\345\275\225", nullptr));
#endif // QT_NO_TOOLTIP
        actSubmit->setText(QApplication::translate("MainWindow", "\344\277\235\345\255\230", nullptr));
#ifndef QT_NO_TOOLTIP
        actSubmit->setToolTip(QApplication::translate("MainWindow", "\344\277\235\345\255\230\344\277\256\346\224\271", nullptr));
#endif // QT_NO_TOOLTIP
        actRevert->setText(QApplication::translate("MainWindow", "\345\217\226\346\266\210", nullptr));
#ifndef QT_NO_TOOLTIP
        actRevert->setToolTip(QApplication::translate("MainWindow", "\345\217\226\346\266\210\344\277\256\346\224\271", nullptr));
#endif // QT_NO_TOOLTIP
        actRecDelete->setText(QApplication::translate("MainWindow", "\345\210\240\351\231\244", nullptr));
#ifndef QT_NO_TOOLTIP
        actRecDelete->setToolTip(QApplication::translate("MainWindow", "\345\210\240\351\231\244\350\256\260\345\275\225", nullptr));
#endif // QT_NO_TOOLTIP
        actPhoto->setText(QApplication::translate("MainWindow", "\350\256\276\347\275\256\347\205\247\347\211\207", nullptr));
#ifndef QT_NO_TOOLTIP
        actPhoto->setToolTip(QApplication::translate("MainWindow", "\350\256\276\347\275\256\347\205\247\347\211\207", nullptr));
#endif // QT_NO_TOOLTIP
        actPhotoClear->setText(QApplication::translate("MainWindow", "\346\270\205\351\231\244\347\205\247\347\211\207", nullptr));
#ifndef QT_NO_TOOLTIP
        actPhotoClear->setToolTip(QApplication::translate("MainWindow", "\346\270\205\351\231\244\347\205\247\347\211\207", nullptr));
#endif // QT_NO_TOOLTIP
        actScan->setText(QApplication::translate("MainWindow", "\346\266\250\345\267\245\350\265\204", nullptr));
#ifndef QT_NO_TOOLTIP
        actScan->setToolTip(QApplication::translate("MainWindow", "\346\266\250\345\267\245\350\265\204", nullptr));
#endif // QT_NO_TOOLTIP
        groupBox_3->setTitle(QString());
        groupBoxSort->setTitle(QApplication::translate("MainWindow", "\346\216\222\345\272\217", nullptr));
        label_14->setText(QApplication::translate("MainWindow", "\346\216\222\345\272\217\345\255\227\346\256\265", nullptr));
        radioBtnAscend->setText(QApplication::translate("MainWindow", "\345\215\207\345\272\217", nullptr));
        radioBtnDescend->setText(QApplication::translate("MainWindow", "\351\231\215\345\272\217", nullptr));
        groupBoxFilter->setTitle(QApplication::translate("MainWindow", "\346\225\260\346\215\256\350\277\207\346\273\244", nullptr));
        radioBtnMan->setText(QApplication::translate("MainWindow", "\347\224\267", nullptr));
        radioBtnWoman->setText(QApplication::translate("MainWindow", "\345\245\263", nullptr));
        radioBtnBoth->setText(QApplication::translate("MainWindow", "\345\205\250\346\230\276\347\244\272", nullptr));
        groupBox->setTitle(QString());
        label_2->setText(QApplication::translate("MainWindow", "\345\247\223  \345\220\215", nullptr));
        dbComboSex->setItemText(0, QApplication::translate("MainWindow", "\347\224\267", nullptr));
        dbComboSex->setItemText(1, QApplication::translate("MainWindow", "\345\245\263", nullptr));

        label_3->setText(QApplication::translate("MainWindow", "\346\200\247  \345\210\253", nullptr));
        label_9->setText(QApplication::translate("MainWindow", "\345\244\207   \346\263\250", nullptr));
        label_12->setText(QApplication::translate("MainWindow", "\345\267\245  \350\265\204", nullptr));
        dbSpinSalary->setPrefix(QString());
        dbComboDep->setItemText(0, QApplication::translate("MainWindow", "\351\224\200\345\224\256\351\203\250", nullptr));
        dbComboDep->setItemText(1, QApplication::translate("MainWindow", "\346\212\200\346\234\257\351\203\250", nullptr));
        dbComboDep->setItemText(2, QApplication::translate("MainWindow", "\347\224\237\344\272\247\351\203\250", nullptr));
        dbComboDep->setItemText(3, QApplication::translate("MainWindow", "\350\241\214\346\224\277\351\203\250", nullptr));

        label_6->setText(QApplication::translate("MainWindow", "\351\203\250  \351\227\250", nullptr));
        label->setText(QApplication::translate("MainWindow", "\345\267\245  \345\217\267", nullptr));
        label_7->setText(QApplication::translate("MainWindow", "\345\207\272\347\224\237\347\234\201\344\273\275", nullptr));
        dbComboProvince->setItemText(0, QApplication::translate("MainWindow", "\345\214\227\344\272\254", nullptr));
        dbComboProvince->setItemText(1, QApplication::translate("MainWindow", "\344\270\212\346\265\267", nullptr));
        dbComboProvince->setItemText(2, QApplication::translate("MainWindow", "\345\244\251\346\264\245", nullptr));
        dbComboProvince->setItemText(3, QApplication::translate("MainWindow", "\351\207\215\345\272\206", nullptr));
        dbComboProvince->setItemText(4, QApplication::translate("MainWindow", "\345\256\211\345\276\275", nullptr));
        dbComboProvince->setItemText(5, QApplication::translate("MainWindow", "\346\262\263\345\214\227", nullptr));
        dbComboProvince->setItemText(6, QApplication::translate("MainWindow", "\346\262\263\345\215\227", nullptr));
        dbComboProvince->setItemText(7, QApplication::translate("MainWindow", "\346\271\226\345\214\227", nullptr));
        dbComboProvince->setItemText(8, QApplication::translate("MainWindow", "\346\271\226\345\215\227", nullptr));
        dbComboProvince->setItemText(9, QApplication::translate("MainWindow", "\345\261\261\350\245\277", nullptr));
        dbComboProvince->setItemText(10, QApplication::translate("MainWindow", "\345\261\261\344\270\234", nullptr));
        dbComboProvince->setItemText(11, QApplication::translate("MainWindow", "\351\231\225\350\245\277", nullptr));
        dbComboProvince->setItemText(12, QApplication::translate("MainWindow", "\346\261\237\350\213\217", nullptr));
        dbComboProvince->setItemText(13, QApplication::translate("MainWindow", "\346\261\237\350\245\277", nullptr));

        label_5->setText(QApplication::translate("MainWindow", "\345\207\272\347\224\237\346\227\245\346\234\237", nullptr));
        dbEditBirth->setDisplayFormat(QApplication::translate("MainWindow", "yyyy-MM-dd", nullptr));
        label_13->setText(QApplication::translate("MainWindow", "\347\205\247  \347\211\207", nullptr));
        dbLabPhoto->setText(QApplication::translate("MainWindow", "dbLabPhoto", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
