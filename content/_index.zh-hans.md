---
title: "Briar 用户手册"
---

# Briar 是什么？

Briar 是一款为活动人士、记者和其他需要安全、轻松和强大的通信方式的人设计的消息应用。与传统的消息应用不同，Briar 不依赖中央服务器——消息在用户设备之间直接同步。即便互联网中断，Briar 也可以通过蓝牙或 Wi-Fi 进行同步，在危机中保持信息流通。如果互联网连接正常，Briar 可以通过 Tor 网络进行同步，从而保护用户及其关系不受监视。

# 安装

运行安卓系统的设备可从Google Play下载Briar, 地址(https://play.google.com/store/apps/details?id=org.briarproject.briar.android)

>**提示：**如果不确定是否有Android设备，请检查其是否有Play商店应用。如果是这样，该设备运行的是Android系统

如果您拥有的是Android设备，但不想使用Google Play，Briar网站上有通过[F-Droid](https://briarproject.org/fdroid.html)或者[直接下载] APK文件（https://briarproject.org/fdroid.html）安装该应用程序的说明 

# 创建帐户

！[创建帐户](/img/create-account.png)

首次打开Briar时，您会被要求创建一个帐户。您可以选择任何昵称和密码。密码长度至少为8个字符，并且应该难以猜测。

> **警告：**您的Briar帐户安全地存储在设备上，而不是云中。如果您卸载Briar或忘记密码，将无法恢复您的帐户。

点击“创建帐户”。创建帐户后，您将被带到联系人列表

{{< break-do-not-translate >}}

# 添加联系人

！[添加联系人的选项](/img/add-contact-options-cropped.png)

要添加联系人，请点击联系人列表右下方的加号图标

在出现的两个选项中选择一个 

{{< break-do-not-translate >}}

## 添加远处的联系人

![远距离添加联系人](/img/add-contact-remotely.png)

复制<code>briar://</code>链接并将它发给你想要添加的人
您也可以使用“共享”按钮选择用于发送链接的应用。

将您从你想要添加的人那里接收到的链接粘贴到下方的文本框中
单击“继续”，然后为新联系人选择一个昵称。

接下来，您将看到通知您每个待处理联系人状态的“待处理的联系人请求”屏幕
Briar将尝试定期连接到您的联系人以添加他们

连接成功后，您将被添加到彼此的联系人列表中。
恭喜！您已准备好安全地进行交流

如果Briar在48小时后无法连接到您的联系人，则待处理的联系人列表将显示“添加联系人失败”的消息。 双方都应该从彼此的列表中删除待处理的联系人，然后再次添加彼此的链接。

{{< break-do-not-translate >}}

![待处理联系人](/img/add-contact-pending-cropped.png)

{{< break-do-not-translate >}}

## 添加附近的联系人

![添加一个联系人, 步骤1](/img/add-contact-1.png)

添加联系人的另一种方法是与您要添加的人会面。你们每个人都将从对方的屏幕扫描二维码。这样可以确保您与正确的人连接，因此没有其他人可以冒充您或阅读您的消息。

准备您准备好开始时，点击“继续”。

{{< break-do-not-translate >}}

![添加一个联系人，步骤2](/img/add-contact-2.png)

在取景器中对齐您联系人的二维码。您可能需要等待几秒钟，相机才能对焦 

相机扫描二维码后，您会看到“等待联系人扫描和连接”的消息。现在您的联系人应该扫描您的二维码。

{{< break-do-not-translate >}}

![显示一名新添加联系人的联系人列表](/img/contact-list-with-contact-cropped.png)

你们的设备将交换信息，并将在几秒钟后将被添加到彼此的联系人列表中。恭喜！你们已准备好安全地进行交流。

{{< break-do-not-translate >}}

# 消息##

![私人讯息对话](/img/manual_messaging-cropped.png)

要发送私人消息，请在联系人列表中点击联系人的名字

> **提示:** Briar中的所有消息都是端到端加密的，因此没有其他人可以阅读它们

如果您的联系人处于离线状态，那么下次你们俩都在线时，您的消息就会发送出去。

{{< break-do-not-translate >}}

# 介绍联系人##

![开始一段介绍](/img/introduction-1-cropped.png)

您可以通过Briar互相介绍联系人。这使他们无需见面即可成为联系人。要开始介绍，请在联系人列表中点击联系人的姓名，然后从菜单中选择“进行介绍”。 

{{< break-do-not-translate >}}

![选择第二联系人](/img/introduction-2-cropped.png) 

接下来，选择您要介绍的其他联系人 

{{< break-do-not-translate >}}

![向双方联系人添加一条消息](/img/introduction-3-cropped.png)

向联系人添加一条可选消息，然后点击“进行介绍”。

{{< break-do-not-translate >}}

![一个介绍请求](/img/introduction-5-cropped.png)

您的联系人将看到一条消息，询问他们是否接受介绍。如果他们俩都接受，他们将被添加到彼此的联系人列表中，并且可以安全地进行交流。

{{< break-do-not-translate >}}

# 私人群 ## 

![选中展示私人群特性的主菜单](/img/nav-drawer-private-groups.png)

您可使用Briar与您的联系人进行群聊。要创建一个群组，请打开主菜单并选择“私人群”，接着私人群列表将会打开。点击加号图标创建一个新群。

{{< break-do-not-translate >}}

![创建一个私人群，步骤1](/img/create-private-group-1-cropped.png)

为您的群选择一个名称，接着点按“新建群”

{{< break-do-not-translate >}}

![创建一个私人群，步骤2](/img/create-private-group-2-cropped.png)

接下来，请选择您想要邀请入群的联系人。选好后，请按checkmark图标。

{{< break-do-not-translate >}}

![创建一个私人群，步骤3](/img/create-private-group-3-cropped.png)

向选择的联系人添加一条可选消息，然后点击“发送邀请”。联系人将看到一条邀请他们加入的消息。

{{< break-do-not-translate >}}

![示新创建的群的私人群列表](/img/create-private-group-4-cropped.png)

新群将被添加到您的私人群列表中。这个列表显示了您所属的所有群组。

{{< break-do-not-translate >}}

![一个私人群中的一个对话](/img/private-group-2.png)

私人群中的消息被组织成帖子。任何成员都可以回复一条消息或新建一个帖子。

群的创建者是唯一可以邀请新成员的人。任何成员都可以离开这个群。如果创建者离开，该群将被解散。

{{< break-do-not-translate >}}

# 论坛

![选中展示论坛功能的主菜单](/img/nav-drawer-forums.png)

论坛是公开的对话。与私人群不同，任何加入一个论坛的人都可以邀请自己的联系人。

要创建一个论坛，打开主菜单，选择"论坛"。论坛列表将打开。点击加号图标创建一个新论坛。

{{< break-do-not-translate >}}

![正创建一个论坛](/img/create-forum-1-cropped.png)

为您的论坛选择一个名字，接着点击“创建论坛”

{{< break-do-not-translate >}}

![展示一个新创建论坛的论坛列表](/img/create-forum-2-cropped.png)

新论坛将添加到您的论坛列表中。此列表显示您所属的所有论坛。 

{{< break-do-not-translate >}}

![分享一个论坛，步骤1](/img/share-forum-1-cropped.png)

要与您的联系人共享论坛，请点击该论坛以将其打开，然后点击共享图标。 

{{< break-do-not-translate >}}

![分享一个论坛，步骤2](/img/share-forum-2-cropped.png)

接下来，选择您要与之共享论坛的联系人。完成后，按对勾图标。 

{{< break-do-not-translate >}}

![分享一个论坛，步骤3](/img/share-forum-3-cropped.png)

向所选联系人添加一条可选消息，然后点击“共享论坛”。联系人将看到一条消息，邀请他们加入。

{{< break-do-not-translate >}}

![论坛中的一个会话](/img/forum-1.png)

论坛中的消息组织成多个主题。任何成员都可以回复一条消息或开新帖。

论坛的任何成员都可以邀请新成员，包括创建者在内的任何成员都可以离开论坛。论坛继续存在，直到最后一位成员离开为止。 

{{< break-do-not-translate >}}

# 博客

{{< break-do-not-translate >}}

![展示选中的播客功能的主菜单](/img/nav-drawer-blogs.png)

您的Briar帐户有一个内置博客。您可以使用它发布有关您生活的新闻和更新。您的博客会自动与您的联系人共享，他们的博客也会与您共享。

要阅读联系人的博客或撰写帖子，请打开主菜单，然后选择“博客”。 

{{< break-do-not-translate >}}

![写一篇博文，步骤1](/img/write-blog-post-1-cropped.png)

要撰写一篇帖子，请点击博客源顶部的笔形图标。

{{< break-do-not-translate >}}

![写一篇博文，步骤2](/img/write-blog-post-2-cropped.png)

撰写您的博文，然后点击“发布”

{{< break-do-not-translate >}}

![展示一篇新创建博文的博客源](/img/write-blog-post-3-cropped.png)

您的新文章将显示在博客源中

{{< break-do-not-translate >}}

![转载一篇博文，步骤1](/img/reblog-1-cropped.png)

要转载一篇播客文章，请点击文章角落的转载图标。

{{< break-do-not-translate >}}

![转载一篇博文，步骤2](/img/reblog-2-cropped.png)

添加一条可选注释，然后点击“转载”。

{{< break-do-not-translate >}}

![转载一篇博文，步骤3](/img/reblog-3-cropped.png)

转载的博文将显示在博客源中，并附上您的评论

{{< break-do-not-translate >}}

# RSS源 

您可以使用Briar阅读任何发布RSS源的博客或新闻站点。文章通过Tor下载，以保护您的隐私。您可以对RSS源中的文章进行转载和评论，就像您可以对博客文章做的事一样。

> **提示:** RSS是网站以易于转载的形式发布文章的一种方式。

{{< break-do-not-translate >}}

![导入一个RSS源，步骤1](/img/import-rss-feed-1-cropped.png)

要导入一个RSS源，请打开博客源，然后从菜单中选择“导入RSS源”。

{{< break-do-not-translate >}}

![导入一个RSS源，步骤2](/img/import-rss-feed-2-cropped.png)

输入RSS源的URL，然后点击“导入”。文章将被下载并添加到博客源中。这可能需要花掉几分钟。

{{< break-do-not-translate >}}

![展示一篇新导入RSS文章的博客源](/img/import-rss-feed-3-cropped.png)

新文章发布后，Briar将自动下载它们。除非选择转载，否则导入的文章不会与您的联系人共享。

{{< break-do-not-translate >}}

![管理RSS源，步骤1](/img/manage-rss-feeds-1-cropped.png)

要管理您的RSS源，请打开博客源，然后从菜单中选择“管理RSS源”。

{{< break-do-not-translate >}}

![管理RSS源，步骤2](/img/manage-rss-feeds-2-cropped.png) 

要删除一个源，请点击垃圾桶图标。除了您转载的文章外，导入的文章将从博客源中被删除。

{{< break-do-not-translate >}}

# 删除联系人#

![删除一位联系人](/img/delete-contact-cropped.png)

要删除一位联系人，请在联系人列表中点击该联系人的姓名，然后从菜单中选择“删除联系人”。

> **提示:** 为了保护您的隐私，不会通知该联系人您已将其删除。从现在起，您对该联系人显示的状态将始终为“离线”

{{< break-do-not-translate >}}

# 设置

![设置列表](/img/manual_dark_theme_settings-cropped.png)

要查找设置，请打开主菜单，然后选择“设置”。
在这里您可以自定义您的Briar体验

{{< break-do-not-translate >}}

## 主题

![深色主题的主菜单](/img/manual_dark_theme_nav_drawer-cropped.png)

您可更改Briar使用的配色方案：

* **浅色** Briar将使用浅色
* **深色:** Briar将使用深色
* **自动:** Briar将根据一天中的时间更改其配色方案
* **系统默认:** Briar将使用系统的配色方案

{{< break-do-not-translate >}}

## 通过互联网连接（Tor）

![设置屏幕的“网络”部分](/img/manual_tor_settings-cropped.png)

> **提示:** Briar使用Tor来连接到互联网。 Tor是由世界各地的志愿者运行的计算机网络，旨在帮助人们在没有审查的情况下私​私密地访问互联网。“网桥”是可以在您的政府或互联网提供商阻止它的情况下帮助您连接到Tor的计算机。

您可以控制Briar如何连接到互联网：

* **根据位置自动** Briar将根据您当前的位置选择如何连接
* **在没有网桥情况下使用Tor:** Briar将不使用网桥连接到Tor网络
* **通过网桥使用Tor:** Briar将使用网桥连接到Tor
* **不连接:** Briar根本不会连接到互联网

## 使用移动数据

您可以控制Briar是否使用移动数据。如果关闭移动数据，则Briar仅在您连接到Wi-Fi时才使用互联网。

## 仅在充电时通过互联网（Tor）连接

您可以控制Briar在设备依靠电池供电时是否使用互联网。如果启用此设置，则Briar仅在设备连接电源后才能使用互联网。

## 屏幕锁

![设置屏幕的“安全性”部分](/img/manual_app_lock-cropped.png)

> **提示:** 此功能在Android版本4上不可用

为了在其他人使用您的设备时保护您的隐私，您可以不登出账户情况而锁定Briar。这样可以防止Briar在您输入PIN，图案或密码之前被使用。

Briar所用的PIN，图案或密码与通常用来解锁设备的相同，因此，如果您尚未选择PIN，图案或密码，则此设置将被禁用（显示为灰色）。您可以使用设备的“设置”应用选择一个。

![展示'锁定应用'选项的主菜单](/img/manual_app_lock_nav_drawer-cropped.png)

当锁频设置处于激活状态，“锁定应用”选项将被添加到Briar的主菜单中。您可以使用此选项在不登出账户情况下锁定Briar

{{< break-do-not-translate >}}

![解锁Briar](/img/manual_app_lock_keyguard.png)

当Briar处于锁定状态，您会被要求输入PIN码，图案或密码来解锁它

{{< break-do-not-translate >}}

## 屏幕锁定不活动超时 

> **提示:** 此功能在Android版本4上不可用 

当Briar在一段时间内未被使用，您可选择自动锁定Briar
