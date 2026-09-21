import { Link } from "react-router-dom";

function Navbar(){

    return (

        <nav className="flex flex-row shadow-sm h-20 py-2 px-4">
               <div className="flex-1 flex items-center ">
                 <h5 className="text-purple-800 font-bold text-lg">VoxInterview</h5>
               </div>
               <div className="flex-1 flex items-center justify-center gap-4">
                  <Link  to="/"> How it Works</Link>
                  <Link  to="/feature">Features</Link>
                  <Link  to="/practice">Practice</Link>
                  <Link  to="/login">SignIn</Link>
               </div>
               <div className="flex-1 flex items-center justify-end ">
                   <Link to="/" className="bg-purple-800 px-4 py-2 text-sm
                             rounded-lg text-white">Start Interview</Link>
               </div>
        </nav>

    )
}
export default Navbar;