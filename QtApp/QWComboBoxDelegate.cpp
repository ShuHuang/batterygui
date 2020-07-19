#include "QWComboBoxDelegate.h"

#include    <QComboBox>

QWComboBoxDelegate::QWComboBoxDelegate(QObject *parent):QStyledItemDelegate(parent)
{

}

void QWComboBoxDelegate::setItems(QStringList items, bool isEdit)
{
}

QWidget *QWComboBoxDelegate::createEditor(QWidget *parent,
       const QStyleOptionViewItem &option, const QModelIndex &index) const
{
}

void QWComboBoxDelegate::setEditorData(QWidget *editor, const QModelIndex &index) const
{
}

void QWComboBoxDelegate::setModelData(QWidget *editor, QAbstractItemModel *model, const QModelIndex &index) const
{
}

void QWComboBoxDelegate::updateEditorGeometry(QWidget *editor,
                const QStyleOptionViewItem &option, const QModelIndex &index) const
{
}
