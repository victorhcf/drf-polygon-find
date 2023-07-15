from django.core.urlresolvers import reverse
from admin_tools.menu import items, Menu

class MyMenu(Menu):
    def __init__(self, **kwargs):
        super(MyMenu, self).__init__(**kwargs)
        self.children += [
            items.MenuItem('Home', reverse('admin:index')),
            items.AppList('Applications'),
            items.MenuItem('Multi level menu item',
                children=[
                    items.MenuItem('Child 1', '/foo/'),
                    items.MenuItem('Child 2', '/bar/'),
                ]
            ),
        ]