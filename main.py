from nicegui import ui,app
from sections import hero,welcome,Discover,gallery

app.add_static_files("/assets", "assets")

ui.add_head_html('''
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
''')




hero.render()
welcome.render()
Discover.discover()
gallery.gallery()

ui.run()