#include "mbtool.h"
#include "ui_mbtool.h"

mbtool::mbtool(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::mbtool)
{
    ui->setupUi(this);
}

mbtool::~mbtool()
{
    delete ui;
}

void mbtool::on_import_root_btn_clicked()
{

}
