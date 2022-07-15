// $(document).ready( function (e){
//     $('.add_to_cart').on('click', function(e){
        
//         e.preventDefault()
//         let product_id = $(this).attr('data-id')
//         let product_quantity = $(this).attr('product_quantity')
//         alert('salom')

//         $.ajax({
          
//             url:"http://localhost:8000/order/add_to_cart/",
//             type: "POST",
//             data: {
//                 product: product, 
//             },
//             success: function (data){
//                 $(".cart_html").data(data)
//             },
//             error: function(data){
//                 alert('error')
//             }
           
//         }) 
//     })    

// })