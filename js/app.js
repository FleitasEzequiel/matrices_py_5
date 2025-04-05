const express = require("express")
const cors = require("cors")
const app = express()

app.use(express.json())
app.use(cors({
  methods: ["GET","POST"],
  credentials: true,
  origin:"http://localhost:8080"
}))
app.use(express.urlencoded({ extended: true }));



app.post("/",(req,res)=>{
  const {matriz1, matriz2} = req.body
  const filas1 = matriz1[0].length;
  const columnas2 = matriz2.length;
  const columnas1 = matriz1.length;
  const matrizResultado = new Array(filas1);
  for (let i = 0; i < filas1; i++) {
    matrizResultado[i] = new Array(columnas2).fill(0);
  }
  
  try {
    for (let i = 0; i < filas1; i++) {
        for (let j = 0; j < columnas2; j++) {
            for (let k = 0; k < columnas1; k++) {
                matrizResultado[i][j] += matriz1[i][k] * matriz2[k][j];
            }
        }
    }
    res.json({resultado:matrizResultado})
  } catch (error) {
    console.log(error)
    res.status(500)
  }
    // Realizar la multiplicación

})

const port = 4500
app.listen(port,()=>{
  console.log("Servidor iniciado en el puerto", port)
})