from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.name_input = TextInput(hint_text='Enter your name', multiline=False)
        layout.add_widget(self.name_input)
        
        save_btn = Button(text='Save', size_hint_y=None, height=50)
        save_btn.bind(on_press=self.save_data)
        layout.add_widget(save_btn)
        
        show_btn = Button(text='Show Data', size_hint_y=None, height=50)
        show_btn.bind(on_press=self.show_data)
        layout.add_widget(show_btn)
        
        self.result_label = Label(text='', font_size=20)
        layout.add_widget(self.result_label)
        
        return layout
    
    def save_data(self, instance):
        store = JsonStore('data.json')
        name = self.name_input.text
        if name:
            store.put('user', name=name)
            self.result_label.text = f'Saved: {name}'
            self.name_input.text = ''
        else:
            self.result_label.text = 'Please enter a name'
    
    def show_data(self, instance):
        store = JsonStore('data.json')
        if store.exists('user'):
            user = store.get('user')
            self.result_label.text = f'Name: {user["name"]}'
        else:
            self.result_label.text = 'No data saved'

if __name__ == '__main__':
    MyApp().run()
