import { Outlet } from "react-router-dom";
import Footer from "../components/Footer";
import Navbar from "../components/Navbar";

function PublicLayout(){
  return(
    <div className="min-h-screen flex flex-col bg-white">
            <Navbar/>
                <main className="flex-1 
                        flex flex-col m-5 ">
                        <Outlet/>
                </main>
            <Footer/>
    </div>

  )
   
}
export default PublicLayout;