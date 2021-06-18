import Client from './Client.js';
const resource = ''

export default {
    getBooks(payload) {
        let url = `${resource}`
        
        let headers = {}

        return Client.get(url, payload, headers)
    }
}