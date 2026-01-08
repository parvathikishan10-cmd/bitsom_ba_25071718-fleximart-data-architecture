// Task 2.2: MongoDB Operations Implementation

// Operation 1: Load Data
// mongoimport --db fleximart --collection products --file products_catalog.json --jsonArray

// Operation 2: Basic Query
// Find Electronics < 50,000; return name, price, stock
db.products.find(
    { category: "Electronics", price: { $lt: 50000 } },
    { name: 1, price: 1, stock: 1, _id: 0 }
);

// Operation 3: Review Analysis
// Find products with average rating >= 4.0
db.products.aggregate([
    { $addFields: { avg_rating: { $avg: "$reviews.rating" } } },
    { $match: { avg_rating: { $gte: 4.0 } } }
    { $project: {_id: 0, name: 1, avg_rating: 1}}
]);

// Operation 4: Update Operation
// Add a new review to ELEC001
db.products.updateOne(
    { product_id: "ELEC001" },
    { $push: { 
        reviews: { user: "U999", rating: 4, comment: "Good value", date: new Date() } 
      } 
    }
);

// Operation 5: Complex Aggregation
// Average price by category sorted descending
db.products.aggregate([
    {
        $group: {
            _id: "$category",
            avg_price: { $avg: "$price" },
            product_count: { $sum: 1 }
        }
    },
    { $sort: { avg_price: -1 } },
    { $project: { category: "$_id", avg_price: 1, product_count: 1, _id: 0 } }
]);
