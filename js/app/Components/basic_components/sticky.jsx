import React from 'react';

export class Sticky extends React.Component {

  componentDidMount() {
    const setInitialHeights = (elements) => {
      [].forEach.call(elements, (sticky) => {
        sticky.setAttribute('data-sticky-initial', sticky.getBoundingClientRect().top);
      });
    };

    const stickies = document.querySelectorAll('[data-sticky]');
    setInitialHeights(stickies);

    const footer = document.querySelectorAll("footer")[0];

    document.addEventListener('scroll', () => {
      const top = document.documentElement.scrollTop || document.body.scrollTop;
      const bottom = document.documentElement.scrollHeight || document.body.scrollHeight;

      [].forEach.call(stickies, (sticky) => {
        const stickyInitial = parseInt(sticky.getAttribute('data-sticky-initial'), 10);
        const stickyEnter = parseInt(sticky.getAttribute('data-sticky-enter'), 10) || stickyInitial;
        const stickyExit = parseInt(sticky.getAttribute('data-sticky-exit'), 10) || bottom;

        if (top >= stickyEnter && top <= stickyExit) {
          sticky.classList.add('sticky');
        } else {
          sticky.classList.remove('sticky');
        }

        if (footer.getBoundingClientRect().top <= 55) {
          sticky.classList.remove('sticky')
        }
      });
    });
  }

  render() {
    const { className, enter, exit, children } = this.props;
    return (
      <div className={`Sticky ${className}`}
            data-sticky
            data-sticky-enter={enter}
            data-sticky-exit={exit}>

        {children}
      </div>
    )
  }
}

Sticky.propTypes = {
  className: React.PropTypes.string,
  enter: React.PropTypes.string,
  exit: React.PropTypes.string,
  children: React.PropTypes.node,
}
