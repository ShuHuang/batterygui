#include "MainWindow.h"
#include "ui_MainWindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    this->setCentralWidget(ui->splitter);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::do_currentChanged(const QModelIndex &current, const QModelIndex &previous)
{
}

void MainWindow::do_currentRowChanged(const QModelIndex &current, const QModelIndex &previous)
{

}

void MainWindow::on_actOpenDB_triggered()
{
}

void MainWindow::on_actRecAppend_triggered()
{
}

