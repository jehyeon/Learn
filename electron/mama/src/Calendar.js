const calendar = require('calendar-js');

function thisMonth() {
    const today = new Date();
    const month = today.getMonth();
    const year = today.getFullYear();

    return calendar().of(year, month).calendar;
}

function get(year, month) {
    return calendar().of(year, month).calendar;
}

function weekdays() {
    return calendar().weekdaysAbbr();
}

module.exports = {
    thisMonth,
    get,
    weekdays
};