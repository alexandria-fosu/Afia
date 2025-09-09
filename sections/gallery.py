from nicegui import ui

def gallery():
   with ui.grid(columns=3).classes("w-screen h-screen justify-center p-8 gap-12 mx-8 bg-grey-700 items-center"):
        with ui.column().classes("w-72 items-center"):
            ui.image("assets/images/smoothies-3176371_1280.jpg").classes("w-[400px] h-1/2 rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")
            ui.label("NATURAL JUICES").classes("mt-4 text-4xl font-semibold")
            ui.label("Indulge in our refreshing natural juices, prepared with love from the finest ingredients").classes("text-gray-700 text-xl shadow-xl")
        with ui.column().classes("w-72 items-center"):
            ui.image("assets/images/wine-1543170_1280.jpg").classes("w-[400px] h-auto rounded-lg shadow-xl transition-transform duration-300 hover:scale-110")  
            ui.label("THE WINE YOU LOVE").classes("mt-4 text-4xl font-semibold")
            ui.label("Savor our expertly curated selection of wines, perfect to pair with our dishes").classes("text-gray-700 text-xl shadow-xl")
        with ui.column().classes("w-72 items-center shadow-xl"):
            ui.image("assets/images/Untitled design.png").classes("w-[400px] h-auto rounded-lg transition-transform duration-300 hover:scale-110")
            ui.label("DELICIOUS FOOD").classes("mt-4 text-4xl font-semibold")
            ui.label("Treat your taste buds to our mouth-watering menu, featuring an array of flavors to delight your senses.").classes("text-gray-700 text-xl")