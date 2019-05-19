#include "mbreplacer.h"
#include "ui_mbreplacer.h"

mbreplacer::mbreplacer(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::mbreplacer)
{
    ui->setupUi(this);
}

mbreplacer::~mbreplacer()
{
    delete ui;
}

void mbreplacer::on_import_root_btn_clicked()
{

}
