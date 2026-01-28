from kivy.app import App
from kivy.uix.browser import WebView # Solo para Android
from kivy.core.window import Window

class OttoTaskApp(App):
    def build(self):
        # El escáner apunta directo a tu núcleo en la nube
        from android.webkit import WebView
        from android.runnable import run_on_ui_thread

        @run_on_ui_thread
        def create_webview():
            webview = WebView(App.get_running_app().activity)
            webview.getSettings().setJavaScriptEnabled(True)
            webview.getSettings().setDomStorageEnabled(True)
            webview.loadUrl("https://otto-task.onrender.com")
            App.get_running_app().activity.setContentView(webview)

        create_webview()
        return None # El WebView toma el control total

if __name__ == "__main__":
    OttoTaskApp().run()
