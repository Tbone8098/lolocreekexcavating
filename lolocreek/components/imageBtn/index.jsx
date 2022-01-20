import Image from 'next/image';
import Link from 'next/link';
import cx from "classnames";

import StyleCSS from './style.module.css';

const Index = (props) => {
    const { img, alt, width, height, action = {} } = props

    const actionHandler = () => {
        if (action['url']) {
            return <>
                <Link href={action['url']}>
                    <Image
                        src={img}
                        alt={alt}
                        width={width}
                        height={height}
                    />
                </Link>
            </>
        } else {
            return <>
                <Image
                    src={img}
                    alt={alt}
                    width={width}
                    height={height}
                />
            </>
        }
    }

    return (
        <div className={cx(StyleCSS.wrapper)}>
            {actionHandler()}
        </div>
    );
}

export default Index;