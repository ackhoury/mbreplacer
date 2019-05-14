#ifndef MBTOOL_H
#define MBTOOL_H

#include <QMainWindow>

namespace Ui {
class mbtool;
}

class mbtool : public QMainWindow
{
    Q_OBJECT

public:
    explicit mbtool(QWidget *parent = 0);
    ~mbtool();

private slots:
    void on_import_root_btn_clicked();

private:
    Ui::mbtool *ui;
};

#endif // MBTOOL_H
