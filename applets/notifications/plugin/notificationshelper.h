/*
    Copyright (C) 2014  Martin Klapetek <mklapetek@kde.org>

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
*/

#ifndef NOTIFICATIONSHELPER_H
#define NOTIFICATIONSHELPER_H

#include <QObject>
#include <QRect>
#include <QHash>
#include <QVariantMap>

class QQuickWindow;

class NotificationsHelper : public QObject
{
    Q_OBJECT
    Q_PROPERTY(int plasmoidScreen WRITE setPlasmoidScreen)

public:
    NotificationsHelper(QObject *parent = 0);
    ~NotificationsHelper();
    Q_INVOKABLE void addNotificationPopup(QObject *win);
    Q_INVOKABLE QRect workAreaForScreen(int screenId);
    Q_INVOKABLE void closePopup(const QString &sourceName);
    /**
     * Fills the popup with data from notificationData
     * and puts the popup on proper place on screen.
     * If there's no space on screen for the notification,
     * it's queued and displayed as soon as there's space for it
     */
    Q_INVOKABLE void displayNotification(const QVariantMap &notificationData);

    void setPlasmoidScreen(int screenId);

private Q_SLOTS:
    void popupClosed(bool visible);
    void displayQueuedNotification();

private:
    void repositionPopups();

    QList<QQuickWindow*> m_popupsOnScreen;
    QList<QQuickWindow*> m_availablePopups;
    QHash<QString, QQuickWindow*> m_sourceMap;
    QList<QVariantMap> m_queue;
    int m_plasmoidScreen;
    int m_offset;
};

#endif // NOTIFICATIONSHELPER_H