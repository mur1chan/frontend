import { memo } from 'react';
import type { FC } from 'react';

import resets from '../_resets.module.css';
import classes from './Desktop1.module.css';
import { MenuButtonIcon } from './MenuButtonIcon.js';
import { MingcuteScienceLineIcon } from './MingcuteScienceLineIcon.js';

interface Props {
  className?: string;
}
/* @figmaId 1:2 */
export const Desktop1: FC<Props> = memo(function Desktop1(props = {}) {
  return (
    <div className={`${resets.clapyResets} ${classes.root}`}>
      <div className={classes.submitButtonDiv}></div>
      <button className={classes.submit}>Submit</button>      
      <div className={classes.h1}>LOREM IPSUM</div>
      <div className={classes.h2}>Lorem Ipsum Lorem Ipsum</div>
      <div className={classes.inputDiv}></div>
      <div className={classes.inputDiv2}></div>
      <div className={classes.inputField}>Lorem Ipsum</div>
      <div className={classes.inputField2}>Lorem Ipsum</div>
      <div className={classes.rectangle2}></div>
      <div className={classes.menuButton}>
        <MenuButtonIcon className={classes.icon} />
      </div>
      <div className={classes.mingcuteScienceLine}>
        <MingcuteScienceLineIcon className={classes.icon2} />
      </div>
    </div>
  );
});
