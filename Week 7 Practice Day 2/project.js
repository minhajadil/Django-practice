const alluser=()=>{
    fetch("https://fakestoreapi.com/users")
    .then(res=> res.json())
    .then((data)=>{
        data.forEach((element)=>{
            const but= document.getElementById("card-container") ;
            const butto = document.createElement('div') ;
            butto.classList.add("col-sm-3") ;
            butto.innerHTML=` 
            <div class="card m-2">
              <div class="card-body">
                <h5 class="card-title"><a href="" class="text-decoration-none text-dark">${element.username}</a></h5>
                <p class="card-text"></p>
                <h5 class=''>Name :${element.name.firstname} ${element.name.lastname}</h5>
                <h5>
                    Phone : ${element.phone} 
                </h5>
                <a target="_blank"  class="btn btn-warning" href="user_details.html?userid=${element.id}">Details</a>
              </div>
            </div>
        </div>
      ` ;
            but.appendChild(butto) ;
        })

    })
    .catch(err=>console.log(err));  

}
alluser() ;


const specific_details=(id)=>{

    fetch(`https://fakestoreapi.com/users/${id}`)
    .then(res=> res.json())
    .then(element=> {
        const div = document.getElementById('user-details');
        const inner = document.createElement('div');
        inner.classList.add('bg-body-secondary');

        inner.innerHTML=`  <div class="container pt-5">
        <div class="">
          
        <div class="">
            <div class="mb-4">
              <h2>${element.username }</h2>
              <h3 class="text-bold">${element.name.firstname} ${element.name.lastname}</h3>
            </div>
            <div class=' gap-3 p-2'>
           <h4 class='bg-dark text-white '> Phone : ${element.phone} </h4>
           <br/>
           <h4 class='bg-warning w-50 text-center align-items-center '> Address : ${element.address.city} ${element.address.street}  </h4>
           </div>
           ` ;

           div.appendChild(inner) ;

    })

}

const getparams = () => {
    const param = new URLSearchParams(window.location.search).get("userid");
    console.log(param) ;

    specific_details(param) ;
   
  };

  getparams() ;



const handleRegistration=(event)=>{
    event.preventDefault();
    console.log('hello') ;
    const formData = {};

    const formElements = document.getElementById('userForm').elements;
        for (let i = 0; i < formElements.length; i++) {
            const element = formElements[i];

           
            if (element.type !== 'submit') {
                formData[element.name] = element.value;
            }
            // console.log(element)
        }
        fetch('https://fakestoreapi.com/users',{
            method:"POST",
            body:JSON.stringify(
                {
                    email:formData['email'],
                    username:formData['username'],
                    password:formData['password'],
                    name:{
                        firstname:formData['firstname'],
                        lastname:formData['lastname']
                    },
                    address:{
                        city:formData['city'],
                        street:formData['street'],
                        number:formData['number'],
                        zipcode:formData['zipcode'],
                        geolocation:{
                            lat:formData['lat'],
                            long:formData['long']
                        }
                    },
                    phone:formData['phone']
                }
            )
        })
            .then(res=>res.json())
            .then(data=>console.log(data))
}


const handleLogin=(event)=>{
    event.preventDefault();
    console.log('login') ;
    user= document.getElementById("username").value;
    pass= document.getElementById("password").value ;

    fetch('https://fakestoreapi.com/auth/login',{
            method:'POST',
            headers: { "content-type": "application/json" },
            body:JSON.stringify({
                username: user ,
                password: pass
            })
        })
            .then(res=>res.json())
            .then(data=>console.log(data))
}