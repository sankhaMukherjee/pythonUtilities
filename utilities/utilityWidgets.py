from IPython.display import display, HTML
from IPython.html    import widgets

class dispWidget:
   
    def __init__(self, header='Automatic Display System'):
        '''
            This is simply an HTML display widget, and is going to
            contain stuff which you want to be displayed at any
            times
        '''
       
        self.header = widgets.LatexWidget(value=header)
        display(self.header)
        self.header.font_size = '15pt'
        self.header.margin = '5pt'
       
        self.clearButton = widgets.ButtonWidget(description='Clear the Display')
        self.clearButton.on_click( callback = self.clearDisplay )
 
        self.visibleButton = widgets.ButtonWidget(description='Toggle Display')
        self.visibleButton.on_click( callback = self.toggleDisplay )
       
        self.container = widgets.HBox()
        self.container.background_color = '#999999'
        self.container.width = '100%'
        display(self.container)
        self.container.children = [ self.clearButton, self.visibleButton ]
       
        self.textToDisplay = '[-------------- %s -----------]'%header
        self.dispFrame     = widgets.HTMLWidget()
        self.dispFrame.background_color = '#F0F0F0'
        self.dispFrame.margin = '5pt'
        self.dispFrame.width = '100%'
        self.dispFrame.height = '300px'
       
        display(self.dispFrame)
        self.display()
       
        return
   
    def updateDisplay(self, text):
        self.textToDisplay = text
        self.display()
       
    def appendDisplay(self, text):
        self.textToDisplay += '<br>'+text
        self.display()
        
    def prependDisplay(self, text):
        self.textToDisplay = text+'<br>'+self.textToDisplay
        self.display()
       
    def clearDisplay(self, temp='None'):
        self.textToDisplay = '[-------------- %s -----------]'%self.header.value
        self.display()  
 
    def toggleDisplay(self, temp='None'):
       
        if self.dispFrame.visible == False:
            self.dispFrame.visible = True
        else:
            self.dispFrame.visible = False
 
        return
       
    def display(self):
        style = '''
        <style>
        div.scrolled {width:100%; height:100%; overflow:scroll;}
        </style>
        '''
        temp = '<div class="scrolled">'
        temp += self.textToDisplay
        temp += '</div>'
       
        self.dispFrame.value = style + temp 

