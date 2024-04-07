function zadacha3(data) {
    let animalsObj = {};
    let areaObj = {};
    let commands = data.shift().split(": ");
    while(commands[0] !== "EndDay") {
        if(commands[0] === "Add") {
            let [name, food, area] = commands[1].split("-");
            food = Number(food);
            if(name in animalsObj) {
                animalsObj[name].food += food;
            } else {
                animalsObj[name] = {food, area};
            }
            if (!(area in areaObj)) {
                areaObj[area][name] = food;
            } else if (!(name in areaObj[area])) {
                areaObj[area][name] = 1;
            }
        } else if(commands[0] === "Feed") {
            let [name, food, count] = commands[1].split("-");
            if(name in animalsObj) {
                animalsObj[name].food -= food;

                if(animalsObj[name].food <= 0) {
                   delete animalsObj[name];
                   console.log(`${name} was successfully fed`);
                }
            }
        }
        commands = data.shift().split(": ");
    }

    console.log(areaObj)
    let arr = Object.entries(animalsObj);
    console.log(`Animals:`);
    for(let line of arr) {
        console.log(` ${line[0]} -> ${line[1].food}g`);
    }

    console.log(`Areas with hungry animals:`);
    for(let [line, values] of Object.entries(areaObj)) {
        console.log(Object.keys(areaObj[line]))
        console.log(`${line}: ${Object.keys(areaObj[line]).length}`);
    }
}


zadacha3(["Add: Adam-4500-ByTheCreek", "Add: Maya-7600-WaterfallArea", "Add: Maya-1230-WaterfallArea", "Feed: Jamie-2000", "EndDay"])
zadacha3(["Add: Bonie-3490-RiverArea", "Add: Annie-200-RiverArea", "Add: Sam-5430-DeepWoodsArea", "Add: Bonie-200-RiverArea", "Add: Maya-4560-ByTheCreek", "Feed: Maya-2390", "Feed: Bonie-3500", "Feed: Johny-3400", "Feed: Sam-5500", "EndDay"])