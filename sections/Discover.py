from nicegui import ui

def discover():
    with ui.element("div").classes("relative w-full h-[70vh] overfloe-hidden"):
        ui.image("assets/images/wine-2891894.jpg").classes("absolute inset-0 w-full h-full object-cover filter brightness-50")

        with ui.column().classes("absolute inset-0 flex flex-col items-center justify-center text-white text-center"):
            ui.label("Discover").classes("text-2xl italic text-red")
            ui.label("SUNNY SPICE").classes("text-6xl font-bold")

