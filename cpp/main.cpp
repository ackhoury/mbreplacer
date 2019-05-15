#include "mbtool.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    mbtool w;
    w.show();

    return a.exec();
}
