async function analyze(){

let job=document.getElementById("job").value
let files=document.getElementById("resumes").files

let formData=new FormData()

formData.append("job",job)

for(let i=0;i<files.length;i++){
formData.append("resumes",files[i])
}

let response=await fetch("http://127.0.0.1:5000/screen",{
method:"POST",
body:formData
})

let data=await response.json()

let table=document.getElementById("results")

table.innerHTML=""

data.forEach((r,index)=>{

let status="Rejected"

if(index==0) status="Top Candidate"
else if(index<3) status="Shortlisted"

table.innerHTML+=`
<tr>
<td>${r.name}</td>
<td>${r.score}%</td>
<td>${r.skills}</td>
<td>${status}</td>
</tr>
`

})

}