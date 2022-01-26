import Image from 'next/image';
import cx from 'classnames';

// styles
import StyleCSS from './style.module.css';

// images
import { LogoWhite } from 'images';

// components
import { Header, Footer } from 'components';

export default function Index() {
    return (
        <div className='flex flex-col h-screen'>
            <div className='grid grid-cols-12'>
                <div className='col-span-12 md:mt-5'>
                    <Header page="about_us"/>
                </div>
                <div className='col-span-10 col-start-2 flex flex-col place-items-center font-cinzel'>
                    <h1 className='text-4xl text-center md:mb-5 font-libre'>About Us</h1>
                    <div>
                        <div className='my-3 flex justify-center md:float-left md:mr-5'>
                            <div className='w-60'>
                                <Image
                                    src={LogoWhite}
                                    alt='Lolo creek excavating logo'
                                />
                            </div>
                        </div>
                        <div className={cx(StyleCSS.para)}>
                            <p>
                                Lolo Creek Excavating, LLC was started by Brandon Williams in the small town of Lolo, Montana. Brandon has worked in the excavation industry for over 5 years and has experience in a wide variety of construction and excavation applications.
                            </p>
                            <p>
                                Always ready to take on a challenge, we are looking to target both the residential and commercial markets in the Missoula/Bitterroot Valleys and surrounding areas. We know there is a lack of available excavation companies to work on and complete even the smallest projects. That&apos;s why our goal at Lolo Creek Excavating is to alleviate those issues by providing prompt and excellent service to our local area home and business owners.
                            </p>
                            <p>
                                As a new company in the area, we are looking to show the industry that we can&apos;t be beat when it comes to customer service, willingness to go above and beyond, and dedication to making your current and future projects a success.
                            </p>
                            <p>
                                Give Brandon a call anytime to chat about your excavation or snow removal needs, and receive a free quote.
                                (406) 546-9948
                            </p>
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


