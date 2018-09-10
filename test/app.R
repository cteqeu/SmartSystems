#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(quantmod)

# Define UI for application that draws a histogram
ui <- fluidPage(
   
  # Application title
  titlePanel("Stock Charting by Vincent Claes"),
  
  # Sidebar with a slider input for number of bins 
  sidebarLayout(
    sidebarPanel(
      selectInput("stock", "Choose a stock:",
                  list(`StockList` = c("AAPL", "IBM", "ORCL"))
      ),
      textOutput("string1"),
      textOutput("string2")
      
    ),
    
    # Show a plot of the stock
    mainPanel(
      plotOutput("stockPlot"),
      textOutput("MeanStockValue")
    )
  )

)

# Define server logic required to draw a histogram
server <- function(input, output) {
   
  output$stockPlot <- renderPlot({
    stockdata<-getSymbols(input$stock, src="google", auto.assign=FALSE)
    chartSeries(stockdata, theme="white")
    addBBands()
    
  })
  output$MeanStockValue <-renderText({
    stockdata<-getSymbols(input$stock, src="google", auto.assign=FALSE)
    count <-mean(Cl(stockdata),na.rm=TRUE)
    paste("Mean value over time of stock:",count)
  }
  )
  output$string1<-renderText("Please select a stock in the dropdown menu, on the right side you can see the stock price over time with bollingerbands")
  output$string2<-renderText("Below the chart you can see the mean closing price of the stock for this time period")
  
}

# Run the application 
shinyApp(ui = ui, server = server)






