#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_practic.h"

class practic : public QMainWindow
{
    Q_OBJECT

public:
    practic(QWidget *parent = Q_NULLPTR);

private:
    Ui::practicClass ui;
};
