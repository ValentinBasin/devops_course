Query
```json
db.orders.aggregate([
  {
    $group: {
      _id: "$room_type",
      avg_beds: { $avg: "$beds" },
      sum_number_of_reviews: { $sum: "$number_of_reviews" },
      count_bedrooms: { $sum: $bedrooms } 
    }
  }
])
```
