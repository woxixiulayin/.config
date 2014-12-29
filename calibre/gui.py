# preferences for the calibre GUI

### Begin group: DEFAULT
 
# send to storage card by default
# 默认将文件传输到存储卡而非设备内置存储
send_to_storage_card_by_default = False
 
# confirm delete
# 删除前确认
confirm_delete = False
 
# main window geometry
# 主窗口位置尺寸
main_window_geometry = cPickle.loads('\x80\x02csip\n_unpickle_type\nq\x01U\x0cPyQt4.QtCoreq\x02U\nQByteArrayU.\x01\xd9\xd0\xcb\x00\x01\x00\x00\x00\x00\x00\x97\x00\x00\x00H\x00\x00\x04\x9a\x00\x00\x03P\x00\x00\x00\x9f\x00\x00\x00e\x00\x00\x04\x92\x00\x00\x03H\x00\x00\x00\x00\x00\x00\x85\x87Rq\x03.')
 
# new version notification
# 新版程序可用时提示
new_version_notification = True
 
# use roman numerals for series number
# 使用罗马数字作为序列数字
use_roman_numerals_for_series_number = True
 
# sort tags by
# 以名称，流行度，或星级来为标签排序。
sort_tags_by = 'name'
 
# match tags type
# 匹配任意或全部标签
match_tags_type = 'any'
 
# cover flow queue length
# 在浏览模式下显示的书籍封面数量
cover_flow_queue_length = 6
 
# LRF conversion defaults
# 转换到LRF文件的默认选项
LRF_conversion_defaults = cPickle.loads('\x80\x02]q\x01.')
 
# LRF ebook viewer options
# 查看LRF文件的选项
LRF_ebook_viewer_options = None
 
# internally viewed formats
# 使用内置浏览器查看的文件格式
internally_viewed_formats = cPickle.loads('\x80\x02]q\x01(U\x03LRFq\x02U\x04EPUBq\x03U\x03LITq\x04U\x04MOBIq\x05U\x03PRCq\x06U\x03AZWq\x07U\x04HTMLq\x08U\x03FB2q\tU\x03PDBq\nU\x02RBq\x0bU\x03SNBq\x0cU\x05HTMLZq\re.')
 
# column map
# 显示书籍列表时显示的信息列
column_map = cPickle.loads('\x80\x02]q\x01(U\x05titleq\x02U\x08ondeviceq\x03U\x07authorsq\x04U\x04sizeq\x05U\ttimestampq\x06U\x06ratingq\x07U\tpublisherq\x08U\x04tagsq\tU\x06seriesq\nU\x07pubdateq\x0be.')
 
# autolaunch server
# 在程序启动时启动内容服务程序
autolaunch_server = False
 
# oldest news
# 在数据库中保留旧消息
oldest_news = 60
 
# systray icon
# 显示系统托盘图标
systray_icon = False
 
# upload news to device
# 将下载的新闻传输到设备上
upload_news_to_device = True
 
# delete news from library on upload
# Delete news books from library after uploading to device
delete_news_from_library_on_upload = False
 
# separate cover flow
# 将封面显示在单独的窗口而不是在 calibre 主窗口
separate_cover_flow = False
 
# disable tray notification
# 禁用系统托盘消息
disable_tray_notification = False
 
# default send to device action
# 当“传送到设备”按钮被按下时的默认操作
default_send_to_device_action = 'DeviceAction:main::False:False'
 
# asked library thing password
# Asked library thing password at least once.
asked_library_thing_password = False
 
# search as you type
# 输入搜索关键字的同时就进行搜索。如果禁用这个功能，只有在按下回车键后才会开始搜索。
search_as_you_type = False
 
# highlight search matches
# 搜索时在全部书籍列表中以高亮显示标明搜索结果而不是过滤掉不匹配的书籍项。可以按 N 键或 F3 键跳转到下一个匹配项。
highlight_search_matches = False
 
# save to disk template history
# Previously used Save to Disk templates
save_to_disk_template_history = cPickle.loads('\x80\x02]q\x01.')
 
# send to device template history
# Previously used Send to Device templates
send_to_device_template_history = cPickle.loads('\x80\x02]q\x01.')
 
# main search history
# Search history for the main GUI
main_search_history = cPickle.loads('\x80\x02]q\x01.')
 
# viewer search history
# Search history for the ebook viewer
viewer_search_history = cPickle.loads('\x80\x02]q\x01.')
 
# lrf viewer search history
# Search history for the LRF viewer
lrf_viewer_search_history = cPickle.loads('\x80\x02]q\x01.')
 
# scheduler search history
# Search history for the recipe scheduler
scheduler_search_history = cPickle.loads('\x80\x02]q\x01.')
 
# plugin search history
# Search history for the plugin preferences
plugin_search_history = cPickle.loads('\x80\x02]q\x01.')
 
# shortcuts search history
# Search history for the keyboard preferences
shortcuts_search_history = cPickle.loads('\x80\x02]q\x01.')
 
# jobs search history
# Search history for the keyboard preferences
jobs_search_history = cPickle.loads('\x80\x02]q\x01.')
 
# tweaks search history
# Search history for tweaks
tweaks_search_history = cPickle.loads('\x80\x02]q\x01.')
 
# worker limit
# 允许同时进行的格式转换或新闻下载任务的个数。由于软件的某些历史原因，这个值应该设置为实际需要值的两倍。
worker_limit = 6
 
# get social metadata
# 下载社会性元数据(标签、评分等)
get_social_metadata = True
 
# overwrite author title metadata
# 使用新元数据覆盖作者和书名信息
overwrite_author_title_metadata = True
 
# auto download cover
# 自动下载可用封面
auto_download_cover = False
 
# enforce cpu limit
# 将并发任务最大值限制为 CPU 数量
enforce_cpu_limit = True
 
# gui layout
# 软件界面布局。“宽”布局在右侧显示书籍详细信息，“窄”布局在下侧显示书籍详细信息。
gui_layout = 'wide'
 
# show avg rating
# 在标签浏览器中显示每个项目说明的平均星级
show_avg_rating = True
 
# disable animations
# 禁用界面动画
disable_animations = False
 
# tag browser hidden categories
# 标签浏览器分类无法显示
tag_browser_hidden_categories = cPickle.loads('\x80\x02c__builtin__\nset\nq\x01]\x85Rq\x02.')
 


