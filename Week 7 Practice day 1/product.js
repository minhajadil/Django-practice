

const product_details=(id)=>{

    fetch(`https://fakestoreapi.com/products/${id}`)
    .then(res=> res.json())
    .then(element=> {
        const div = document.getElementById('product-details');
        const inner = document.createElement('div');
        inner.classList.add('bg-body-secondary');

        inner.innerHTML=`  <div class="container pt-5">
        <div class="row">
          <div class="col-md-6">
            <img class='p-2' style="height: 400px; width:400px;"
              src="${element.image}"
              class="img-fluid"
              alt="Image"
            />
          </div>
      
          <div class="col-md-6">
            <div class="mb-4">
              <h2>${element.title }</h2>
              <p class="text-muted">${element.description}</p>
            </div>
            <div class=' gap-3 p-2'>
           <h4 class='bg-dark text-white '> Category : ${element.category} </h4>
           <br/>
           <h4 class='bg-warning w-50 text-center align-items-center '> Price : ${element.price} </h4>
           </div>
           ` ;

           div.appendChild(inner) ;

    })

}

const getparams = () => {
    const param = new URLSearchParams(window.location.search).get("product");
    console.log(param) ;
    console.log('hello') ;

    product_details(param) ;
   
  };

  getparams() ;

