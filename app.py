from shiny import render, ui, App

#Page title and tabs
app_ui = ui.page_fluid(
    ui.panel_title("DAM System Analyzer", "DAM System Analyzer"),
    ui.navset_tab(
        ui.nav_panel("Data Cleaned", ""),
        ui.nav_panel("Experiment Analysis", ""),
        ui.nav_panel("Raster Plots", ""),
        ui.nav_menu(
            "Period Analysis",
            ui.nav_panel("Lomb-Scargle", ""),
            ui.nav_panel("Cosinor", ""),
            ui.nav_panel("Chi-Squared", ""),
            ui.nav_panel("Fourier Transform", ""),
            "----",
            "Description:",
            ui.nav_control(
                ui.a("Shiny", href="https://shiny.posit.co", target="_blank")
            ),
        ),
        id="selected_navset_tab",
    ),
    ui.h5("Selected:"),
    ui.output_code("selected"),
)


def server(input, output, session):
    @render.code
    def selected():
        return input.selected_navset_tab()


app = App(app_ui, server)