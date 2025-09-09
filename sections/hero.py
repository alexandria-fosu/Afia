from nicegui import ui, html
ui.add_head_html('''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400..700&display=swap" rel="stylesheet">''')




def render():
    
    with ui.element("div").style("background-image:url(assets/images/breakfast-3765559_1280.jpg) ").classes("h-screen w-screen flex flex-col bg-no-repeat bg-cover bg-center"):
        #navbar
        with ui.element("nav").classes("flex flex-row justtify-between w-screen fixed text-white bg-black/50").style("justify-content:space-around; list-style:none; padding:0; margin:0; Align-items:center; font-size:20px; font-weight:bold; color:#fff "):

            ui.image("assets/images/s.png").style("width:80px; hieght: 50px")

            # navlinks
            navlinks = [{"title": "Home", "path": "/"}, 
                        {"title": "Menu", "path": "/"},
                        {"title": "Reservation", "path": "/"},
                        {"title": "Gallery", "path": "/"},
                        {"title": "About", "path": "/"},
                        {"title": "Contacts", "path": "/"},]
        
            for item in navlinks:
                ui.link(item["title"], item["path"]).classes("no-underline uppercase text-white")
                
            # Using Font Awesome icons for social media
            with ui.row():
                 
                ui.html('<i class= "fa-brands fa-facebook"></i')
                ui.html('<i class= "fa-brands fa-instagram"></i')
                ui.html('<i class= "fa-brands fa-twitter"></i')

            
          #text
        with ui.column().classes("items-center bg-black/50  h-full w-full flex flex-col items-center justify-center"):
            ui.label("Welcome to").style("font-family:dancing script,cursive; font-size:8rem; color:#fff;")
            ui.label("SUNNY SPICE").classes("text-8xl text-white font-bold")
            ui.button("Look Menu").style("border-radius:2px; width:150px").classes("bg-red")


    