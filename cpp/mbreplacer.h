#ifndef MBREPLACER_H
#define MBREPLACER_H

#include <QMainWindow>

namespace Ui {
class mbreplacer;
}

class mbreplacer : public QMainWindow
{
    Q_OBJECT

public:
    explicit mbreplacer(QWidget *parent = 0);
    ~mbreplacer();

private slots:
    void on_import_root_btn_clicked();

private:
    Ui::mbreplacer *ui;
};

#endif // MBREPLACER_H
