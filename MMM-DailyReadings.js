Module.register("MMM-Daily-Readings", {
    // Default module config.
    result: [],
    defaults: {

    },

    start: function() {
        Log.info("Starting module: " + this.name);
        var self = this;

        var configuredVersion = this.config.version;

        self.sendSocketNotification('START', configuredVersion);

        setInterval(function() {
                self.sendSocketNotification('START', configuredVersion);
        }, 3600000); //perform every hour (3600000 milliseconds)
    },

    // Override dom generator.
    getDom: function() {
        Log.log("Updating MMM-Daily_Readings DOM.");

        var verse = "";
        var reference = "";

        if(this.verseOfTheDay != null && this.reference != null){
            verse = this.verseOfTheDay;
            reference = " - " + this.reference;
        }

        var wrapper = document.createElement("div");
        switch (this.config.size) {
            case 'xsmall':
                wrapper.className = "bright xsmall";
                break;
            case 'small':
                wrapper.className = "bright small";
                break;
            case 'medium':
                wrapper.className = "bright";
                break;
            case 'large':
                wrapper.className = "bright large";
                break;
            default:
                wrapper.className = "bright";
        }
        wrapper.innerHTML = verse + reference;
        return wrapper;
        },

    getScripts: function() {
        return [
            this.file('jquery-3.1.1.min.js'),
        ]
    },

    socketNotificationReceived: function(notification, payload) {
        Log.log("socket received from Node Helper");
        if(notification == "Daily_Readings_Result"){
            var json = payload;
            Log.log(payload);
            this.verseOfTheDay = json.votd.text;
            this.reference = json.votd.reference;

            this.updateDom();
        }
    }
});
