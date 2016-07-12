/**
 * @fileoverview
 * @enhanceable
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

goog.provide('proto.VcuWrapperMessage');

goog.require('jspb.Message');
goog.require('proto.Drive');
goog.require('proto.Halt');
goog.require('proto.Orbit');


/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.VcuWrapperMessage = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, proto.VcuWrapperMessage.oneofGroups_);
};
goog.inherits(proto.VcuWrapperMessage, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.VcuWrapperMessage.displayName = 'proto.VcuWrapperMessage';
}
/**
 * Oneof group definitions for this message. Each group defines the field
 * numbers belonging to that group. When of these fields' value is set, all
 * other fields in the group are cleared. During deserialization, if multiple
 * fields are encountered for a group, only the last value seen will be kept.
 * @private {!Array<!Array<number>>}
 * @const
 */
proto.VcuWrapperMessage.oneofGroups_ = [[1,2,3]];

/**
 * @enum {number}
 */
proto.VcuWrapperMessage.MsgCase = {
  MSG_NOT_SET: 0,
  DRIVE: 1,
  ORBIT: 2,
  HALT: 3
};

/**
 * @return {proto.VcuWrapperMessage.MsgCase}
 */
proto.VcuWrapperMessage.prototype.getMsgCase = function() {
  return /** @type {proto.VcuWrapperMessage.MsgCase} */(jspb.Message.computeOneofCase(this, proto.VcuWrapperMessage.oneofGroups_[0]));
};



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.VcuWrapperMessage.prototype.toObject = function(opt_includeInstance) {
  return proto.VcuWrapperMessage.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.VcuWrapperMessage} msg The msg instance to transform.
 * @return {!Object}
 */
proto.VcuWrapperMessage.toObject = function(includeInstance, msg) {
  var f, obj = {
    drive: (f = msg.getDrive()) && proto.Drive.toObject(includeInstance, f),
    orbit: (f = msg.getOrbit()) && proto.Orbit.toObject(includeInstance, f),
    halt: (f = msg.getHalt()) && proto.Halt.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg
  }
  return obj;
};
}


/**
 * Creates a deep clone of this proto. No data is shared with the original.
 * @return {!proto.VcuWrapperMessage} The clone.
 */
proto.VcuWrapperMessage.prototype.cloneMessage = function() {
  return /** @type {!proto.VcuWrapperMessage} */ (jspb.Message.cloneMessage(this));
};


/**
 * optional Drive drive = 1;
 * @return {proto.Drive}
 */
proto.VcuWrapperMessage.prototype.getDrive = function() {
  return /** @type{proto.Drive} */ (
    jspb.Message.getWrapperField(this, proto.Drive, 1));
};


/** @param {proto.Drive|undefined} value  */
proto.VcuWrapperMessage.prototype.setDrive = function(value) {
  jspb.Message.setOneofWrapperField(this, 1, proto.VcuWrapperMessage.oneofGroups_[0], value);
};


proto.VcuWrapperMessage.prototype.clearDrive = function() {
  this.setDrive(undefined);
};


/**
 * optional Orbit orbit = 2;
 * @return {proto.Orbit}
 */
proto.VcuWrapperMessage.prototype.getOrbit = function() {
  return /** @type{proto.Orbit} */ (
    jspb.Message.getWrapperField(this, proto.Orbit, 2));
};


/** @param {proto.Orbit|undefined} value  */
proto.VcuWrapperMessage.prototype.setOrbit = function(value) {
  jspb.Message.setOneofWrapperField(this, 2, proto.VcuWrapperMessage.oneofGroups_[0], value);
};


proto.VcuWrapperMessage.prototype.clearOrbit = function() {
  this.setOrbit(undefined);
};


/**
 * optional Halt halt = 3;
 * @return {proto.Halt}
 */
proto.VcuWrapperMessage.prototype.getHalt = function() {
  return /** @type{proto.Halt} */ (
    jspb.Message.getWrapperField(this, proto.Halt, 3));
};


/** @param {proto.Halt|undefined} value  */
proto.VcuWrapperMessage.prototype.setHalt = function(value) {
  jspb.Message.setOneofWrapperField(this, 3, proto.VcuWrapperMessage.oneofGroups_[0], value);
};


proto.VcuWrapperMessage.prototype.clearHalt = function() {
  this.setHalt(undefined);
};

