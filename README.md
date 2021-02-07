# Uber Eats Scraper
An Uber Eats Selenium web scraper written in python. Gathers info on restaurant name, details, rating, and menu items.
Saves all restaurant urls in a given city and saves data to a json file. Example structure below:

```json
{
  "title": "Osmow's (656 Gardiners Rd Unit 20B)",
  "detail": "$$ • Mediterranean • Sandwich • Salads",
  "rating": "4.4",
  "num_reviews": "(294)",
  "menu": [
    {
      "Picked For You": [
        {
          "name": "Chicken Shawarma Wrap Combo",
          "description": "Finely carved from a rotating spit, chicken thigh roasted to perfection. Served in a pita wrap with choice of fresh ingredients. Topped with Osmow's signature garlic sauce. Comes with drink.",
          "price": "$10.55\n • \n540 - 870 Cal.",
          "status": "In stock",
          "img_url": ""
        },
        {
          "name": "Baklava",
          "description": "A Mediterranean dessert made with phyllo dough and mixed nuts baked to golden perfection, and covered in sweet syrup allowing it to be absorbed into the layers.",
          "price": "$2.87",
          "status": "In stock",
          "img_url": ""
        },
        {
          "name": "Fries",
          "description": "Chopped potatoes deep fried to a moderate crisp",
          "price": "$3.21",
          "status": "In stock",
          "img_url": "https://d1ralsognjng37.cloudfront.net/47b40536-8ecb-4518-b7ac-51ad14570114.jpeg"
        },
        {
          "name": "Falafel",
          "description": "Mix of ground chickpea, fava bean and Osmow’s secret herbs and spices golden fried to perfection and served with Osmow's signature tahini sauce.",
          "price": "$0.99",
          "status": "In stock",
          "img_url": "https://d1ralsognjng37.cloudfront.net/ee41acde-f4a3-4c4d-af8e-c04bea26cfb2.jpeg"
        },
        {
          "name": "Grilled Veggies",
          "description": "Seasonal vegetables garnished with fresh herbs and grilled to perfection.",
          "price": "$6.31",
          "status": "In stock",
          "img_url": "https://d1ralsognjng37.cloudfront.net/4020ee41-077e-4f1b-9e82-34565f121d94.jpeg"
        }
      ]
    }
  ]
}
```

                        

