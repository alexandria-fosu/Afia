from nicegui import ui

def render():
    with ui.grid(columns=2).classes("w-screen h-screen gap-x-12 items-start justify-between items-center"):
        #the left column text
        with ui.column().classes("gap-4 items-center justify-center"):
            ui.label("Ghanaian Restaurant").classes("text-2xl italic text-red-700")
            ui.label("Welcome").classes("text-6xl font-bold mt-2 mb-6")
            ui.label("Every meal is more than just food ...it's a  gathering. we bring together the spirit of Ghanaian hospitality to every plate, serving up authentic dishes made with love and care").classes("text-xl text-gray-600 max-w-lg")

            ui.link("OUR STORY" ).classes("mt-8 text-black font-semibold no-underline text-red")
        with ui.column().classes("w-full item-end"):
            ui.image("assets/images/burger-7419421_1280.jpg").classes("w-[500px] h-[500px] shadow-xl rounded-lg transition-transform duration-300 hover:scale-110")     