import cx from 'classnames'

// style
import StyleCSS from './style.module.css'

// components
import { Header, Logo, Button, Footer } from 'components';

// image
import LoloLogo from 'images/logoWhite.png';

export default function Index() {

    const infoBlock = () => {
        return (
            <div className={cx(StyleCSS.infoBox, 'flex flex-col gap-3')}>
                {/* <h1 className='text-5xl md:text-8xl'>Lolo Excavating</h1> */}
                <p className={cx('text-2xl font-cinzel')}>(123) 456-7890</p>
                <p className='text-sm font-bree'>brandon@lolocreekexcavating.com</p>
                <p className='text-sm font-bree'>1234 Somewhere in Montana Lane</p>
            </div>
        )
    }

    return (
        <div className={cx(StyleCSS.main, 'flex flex-col h-screen')}>
            <div className={cx('grid grid-cols-12')}>
                <div className='col-span-12'>
                    <Header />
                </div>
                <div className='col-span-10 col-start-2'>
                    <div>
                        <div className='mb-3'>
                            <Logo
                                img={LoloLogo}
                            />
                        </div>
                        <div className='mb-3'>
                            {infoBlock()}
                        </div>
                        <div>
                            <Button
                                text="Contact Me"
                                action={{
                                    url: '/contactme'
                                }}
                            />
                        </div>
                    </div>
                </div>
            </div>
            <div className='mt-auto'>
            <Footer />
            </div>
        </div>
    )
}
