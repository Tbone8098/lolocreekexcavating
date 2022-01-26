import cx from 'classnames';
import { useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';

// styles
import StyleCSS from './style.module.css';

// images
import BackwardIcon from 'icons/backward.png';
// import ForwardIcon from 'icons/forward.png';

// components
import { data } from 'datafiles/sideNavData';

const Index = () => {
    const [isOpen, setIsOpen] = useState(false)

    const toggleOpen = () => {
        let temp = isOpen
        setIsOpen(!temp)
    }
    
    const hamburger = () => {
        return (
            <div className={cx(StyleCSS.wrapper)} onClick={toggleOpen}>
                <div className={cx(StyleCSS.hamburger)}>
                    <span></span>
                </div>
            </div>
        )
    }
    
    const menu = () => {
        return (
            <div className={cx(StyleCSS.menu__wrapper)} onClick={toggleOpen}>
                <div className={cx(StyleCSS.menu, 'flex flex-col')} onClick={(e) => e.stopPropagation()}>
                    <div className='mt-4'>
                        <Image
                        alt='close side nav'
                        src={BackwardIcon}
                        width={50}
                        height={50}
                        onClick={toggleOpen}
                        />
                    </div>
                    <ul className='mt-5 mx-1'>
                        {
                            data.map((item, key) => {
                                return (
                                    <li className='mb-3' key={key}>
                                        <div className='place-items-center flex gap-2'>
                                            <Link href={item.url}>
                                            <div className='flex items-center gap-3'>
                                                <Image
                                                alt={item.alt}
                                                src={item.src}
                                                width={item.width}
                                                height={item.height}
                                                />
                                                    {item.title}
                                            </div>
                                            </Link>
                                        </div>
                                    </li>
                                )
                            })
                        }
                    </ul>
                </div>
            </div>
        )
    }

    return (
        <>
            {
                isOpen && menu()
            }
            {hamburger()}
        </>
    );
}

export default Index;