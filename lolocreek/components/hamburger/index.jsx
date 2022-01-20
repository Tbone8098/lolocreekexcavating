import { useState } from 'react';
import cx from "classnames";

// style
import StyleCSS from './style.module.css';

// components
import SideNav from 'components/sideNav'

const Index = () => {
    const [isOpen, setIsOpen] = useState(false)

    const toggle = () => {
        let isOpenClone = !isOpen
        setIsOpen(isOpenClone)
    }

    return (
        <>
            {
                isOpen && <SideNav />
            }
            <div id='navbar__mobile' className='grid md:hidden mx-4' onClick={toggle}>
                <div className={cx(StyleCSS.hamburger)}><span></span></div>
            </div>
        </>
    );
}

export default Index;