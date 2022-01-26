import SnowRemove from 'icons/snowRemoval.png';
import SightWork from 'icons/sitework.png';
import Excavator from 'icons/digger.png';

export const data = [
    {
        title: 'Site Work',
        subtitle: <span className='text-center'>Site <br />Work</span>,
        src: SightWork,
        width: 50,
        height: 50,
        alt: 'Site Work',
        content: <div>
            <ul className='list-disc ml-3'>
                <li>Grading</li>
                <li>Leveling</li>
                <li>Clearing land for development</li>
                <li>Roads – repair and/or maintenance</li>
                <li>Materials – delivery, placement, spreading, and/or haul-off</li>
            </ul>
        </div>
    },
    {
        title: 'Excavation',
        src: Excavator,
        subtitle: <span className='text-center'>Excavation</span>,
        width: 50,
        height: 50,
        alt: 'Excavation',
        content: <div>
            <ul className='list-disc ml-3'>
                <li>Footings</li>
                <li>Septic tanks</li>
                <li>Drain/leach fields</li>
                <li>Ditches</li>
                <li>French drains</li>
                <li>Backfilling</li>
                <li>Driveways – constructing and/or resurfacing</li>
                <li>Building sites – creating and/or leveling</li>

            </ul>
        </div>
    },
    {
        title: 'Snow Removal',
        src: SnowRemove,
        subtitle: <span className='text-center'>Snow <br />Removal</span>,
        width: 50,
        height: 50,
        alt: 'Snow Removal',
        content: 'We have equipment to plow and clear both large or small projects. With our rubber track skid steer, we can clear a lot, road or driveway with ease while being gentle on whatever the surface is. If you have large piles that need to be moved on site or hauled off, we got you.'
    },
]
