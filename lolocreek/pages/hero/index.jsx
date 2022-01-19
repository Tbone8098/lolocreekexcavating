import cx from 'classnames'
import Image from "next/image";

// style
import StyleCSS from './style.module.css'

// components
import Header from 'components/header'
import Logo from 'components/logo'
import Button from 'components/button'
import SideNav2 from 'components/sideNav2';


// images
// import Logo from 'images/lolocreeklogo.png';


export default function Index() {

    const infoBlock = () => {
        return (
            <div className={cx(StyleCSS.infoBox, 'flex flex-col gap-3')}>
                <h1 className='text-5xl md:text-8xl'>Lolo Excavating</h1>
                <h2 className='text-2xl'>406-546-9948</h2>
                <h2 className='text-md'>brandon@lolocreekexcavating.com</h2>
                <h2 className='text-md'>6940 Mormon Creek Rd. Lolo MT 59847</h2>
            </div>
        )
    }

    return (
        <div className={cx(StyleCSS.main, 'h-screen grid grid-cols-12 ')}>
            {/* header for tablet and bigger */}
            <div className='hidden md:inline-block col-span-12 pt-4'>
                <Header />
            </div>
            

            {/* sideNav for mobile */}
            <div className='col-span-9 col-start-2 grid'>
                <div className='place-self-center'>
                    <div className='mb-3'>
                        <Logo
                        width={150}
                        height={150}
                        />
                    </div>
                    {infoBlock()}
                    <div className='flex justify-end'>
                        <Button
                            text="Contact Us"
                            attributes={{
                                'align': 'place-self-end',
                                'background': 'bg-white',
                                'text': 'text-black text-4xl',
                                'border': 'border border-black border-2'
                            }}
                            action={{
                                url: '/contactus'
                            }}
                        />
                    </div>
                </div>
            </div>
            <div className='reletive'>
            <SideNav2 />
            </div>
        </div>
    )
}


// <div className={cx(StyleCSS.main, 'h-screen grid grid-cols-12')}>
//             <div className='col-span-12 h-min pt-4'>
//                 <Header />
//             </div>
//             <div className='col-span-8 col-start-3 md:col-start-2 md:col-span-5 grid'>
//                 <div className='flex flex-col gap-3'>
//                     <div className='md:hidden'>
//                         <Logo />
//                     </div>
//                     {infoBlock()}
//                     <div className='lg:hidden self-end'>
//                         <Button
//                             text="Contact Us"
//                             action={{
//                                 url: '/contactus'
//                             }}
//                             attributes={{
//                                 'text': 'text-3xl text-white'
//                             }}
//                         />
//                     </div>
//                 </div>
//             </div>
//         </div>