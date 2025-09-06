from nicegui import ui

def render():
    with ui.grid(columns=2).classes("w-full gap-x-12 items-start justify-between").style("background-color:e0e1dd;"):
        #the left column text
        with ui.column().classes("gap-4 items-center justify-center"):
             ui.label("Ghanaian Restaurant").classes("text-2xl italic text-red-700")
             ui.label("Welcome").classes("text-6xl font-bold mt-2 mb-6")
             ui.label("Every meal is more than just food ...it's a  gathering. we bring together the spirit of Ghanaian hospitality to every plate, serving up authentic dishes made with love and care").classes("text-xl text-gray-600 max-w-lg")

             ui.link("OUR STORY" ).classes("mt-8 text-black font-semibold no-underline")
        with ui.column().classes("w-full item-end"):
            ui.image("assets/images/burger-7419421_1280.jpg").classes("w-1/2 h-1/2 shadow-xl rounded-lg")     