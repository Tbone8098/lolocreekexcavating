import cx from 'classnames'

// style
import StyleCSS from './style.module.css'

// components
import Header from 'components/header'
import Logo from 'components/logo'
import Button from 'components/button'
import SideNav2 from 'components/sideNav2';
;


export default function Index() {

    const infoBlock = () => {
        return (
            <div className={cx(StyleCSS.infoBox, 'flex flex-col gap-3')}>
                <h1 className='text-5xl md:text-8xl'>Lolo Excavating</h1>
                <h2 className='text-2xl'>(123) 456-7890</h2>
                <h2 className='text-md'>brandon@lolocreekexcavating.com</h2>
                <h2 className='text-md'>1234 Somewhere in Montana Lane</h2>
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
            <SideNav2 />

            <div className='col-span-8 col-start-4 grid'>
                <div className='place-self-center'>
                    <div className='mb-3'>
                        <Logo />
                    </div>
                    {infoBlock()}
                    <div className='flex justify-end'>
                        <Button
                            text="Contact Us"
                            attributes={{
                                'align': 'place-self-end',
                                'background': 'bg-white',
                                'text': 'text-black text-4xl'
                            }}
                            action={{
                                url: '/contactus'
                            }}
                        />
                    </div>
                </div>
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