from nicegui import ui

ui.add_head_html('''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400..700&display=swap" rel="stylesheet">''')



def menu():
   with ui.row().classes("justify-center flex flex-col w-full h-full gap-12 p-8 items-center"):
        ui.label("Discover").classes("text-red text-4xl items-center").style("font-family:dancing script,cursive;")
        ui.label("OUR MENU").classes("text-6xl text-bold items-center")
  
        with ui.element("div").classes("w-full items-center relative h-full overflow-hidden rounded-2xl shadow-lg grid grid-cols-3 gap-hiddden"):
            with ui.column().classes('relative'):
                ui.image("assets/images/noodles-4851996_1280.jpg").classes("w-[500px] h-auto rounded-lg shadow-xl object-cover")
                ui.label("Lunch").classes("absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 items-center text-bold text-2xl") \
                .classes("bg-white text-black px-6 py-2 rounded-full font-bold cursor-pointer w-[130px] h-[50px]")
            with ui.column().classes("relative"):
                ui.image("assets/images/pudding-702960_1280.jpg").classes("w-[500px] h-full rounded-lg shadow-xl object-cover")
                ui.label("Desert").classes("absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 item-center text-bold text-2xl") \
                .classes("bg-white text-black px-6 py-2 rounded-full font-bold w-[130px] h-[50px]")
            with ui.column().classes("relative"):    
                ui.image("assets/images/salad-3477928_1280.jpg").classes("w-[550px] h-auto rounded-lg shadow-xl object-cover")
                ui.label("Starter").classes("absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 items-center text-bold text-2xl") \
                .classes("bg-white text-black px-6 py-2 rounded-full font-bold cursor-pointer w-[130px] h-[50px]") 
            with ui.column().classes("relative"):    
                ui.image("assets/images/grilling-2415223_1280.jpg").classes("w-[500px] h-auto rounded-lg shadow-xl object-cover")
                ui.label("Grills").classes("absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 items-center text-bold text-2xl") \
                .classes("bg-white text-black px-6 py-2 rounded-full font-bold cursor-pointer w-[130px] h-[50px]")
            with ui.column().classes("relative"):
                ui.image("assets/images/burger-7175344_1280.jpg").classes("w-[500px] h-auto rounded-lg shadow-xl object-cover")
                ui.label("Burgers").classes("absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 items-center text-bold text-2xl") \
                .classes("bg-white text-black px-6 py-2 rounded-full font-bold cursor-pointer w-[130px] h-[50px]")
            with ui.column().classes("relative"):
                ui.image("assets/images/drink-4389934_1920.jpg").classes("w-[500px] h-auto rounded-lg shadow-xl object-cover")
                ui.label("Drinks").classes("absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 items-center text-bold text-2xl") \
                .classes("bg-white text-black px-6 py-2 rounded-full font-bold cursor-pointer w-[130px] h-[50px]")
      