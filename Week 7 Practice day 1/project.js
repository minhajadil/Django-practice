const navbar=()=>{


    fetch("https://fakestoreapi.com/products/categories")
    .then(res=>res.json())
    .then((data)=>{
        data.forEach((element)=>{
            const but= document.getElementById("navbuttons") ;
            const butto = document.createElement('div') ;
           
            butto.innerHTML=`<button onclick=products("category/${encodeURIComponent(element)}") class="buttons"> ${element}</button>` ;
            but.appendChild(butto) ;
        })

    })
    .catch(err=>console.log(err));    

}
navbar() ;





const products=(params)=>{


   
    document.getElementById("card-container").innerHTML="" ;



    fetch(`https://fakestoreapi.com/products/${params}`)
    .then(res=>res.json())
    .then((data)=>{
        data.forEach((element)=>{
            const but= document.getElementById("card-container") ;
            const butto = document.createElement('div') ;
            butto.classList.add("col-sm-3") ;
            butto.innerHTML=` 
            <div class="card m-2">
              <div class="card-body">
                <img src="${element.image}" class="card-img-top" ,style="max-width:100%; max_height:100px" alt="...">
                <h5 class="card-title"><a href="" class="text-decoration-none text-dark">${element.title}</a></h5>
                <p class="card-text"></p>
                <p class='text-bg-dark  '>Category :${element.category}</p>
                <h5>
                    Price : ${element.price} $
                </h5>
                <a target="_blank"  class="btn btn-warning" href="product_details.html?product=${element.id}">Details</a>
              </div>
            </div>
        </div>
      ` ;
            but.appendChild(butto) ;
        })

    })
    .catch(err=>console.log(err));    

}
products("") ;












