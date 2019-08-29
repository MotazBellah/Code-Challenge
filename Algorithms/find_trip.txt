function find_start(trips) {
    let start = [];
    let dist = [];

    let first_start = []

    for (let i = 0; i < trips.length; i++) {
        start.push(trips[i][0]);
        dist.push(trips[i][1]);

    }

    for (let i = 0; i < start.length; i++) {
        if(!dist.includes(start[i]) ){
            first_start.push(start[i]);
        }
    }
    return first_start[0];

}

console.log(find_start([['A','B'], ['B','C'], ['C','D']]));
console.log(find_start([['D','E'], ['F','D'], ['E','X'] ]));
console.log(find_start([['Cologne','Berlin'],['Munich','Cologne'],['YourPlace','Munich']]));
